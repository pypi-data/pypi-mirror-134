from .consumer_utils import get_transactional_consumer, consume_message, get_consumer
from .message_utils import shutdown_cleanup
from .producer_utils import get_transactional_producer, produce_message
from nubium_utils.general_utils import parse_headers
from confluent_kafka import TopicPartition
from confluent_kafka import KafkaException
from nubium_utils.confluent_utils.confluent_configs import init_schema_registry_configs
from nubium_utils.custom_exceptions import NoMessageError
import logging
import sys
# from orjson import dumps, loads
# changelog_schema = {"type": "bytes"}
from json import dumps, loads
changelog_schema = {"type": "string"}
from random import random

from copy import deepcopy
from nubium_utils.confluent_utils.rocksb_utils import RDB
from os import environ
from time import sleep

LOGGER = logging.getLogger(__name__)

class RunTableRecovery(Exception):
    def __init__(self):
        pass

class Transaction:
    def __init__(self, message, producer, consumer, metrics_manager):
        self.producer = producer
        self.consumer = consumer
        self.metrics_manager = metrics_manager
        self.message = message
        
        self._committed = False
        self._active_transaction = False

    def key(self):
        return self.message.key()

    def value(self):
        return self.message.value()

    def headers(self):
        return parse_headers(self.message.headers())

    def topic(self):
        return self.message.topic()

    def partition(self):
        return self.message.partition()

    def offset(self):
        return self.message.offset()

    def produce(self, producer_kwargs):
        self.producer.poll(0)
        if not self._active_transaction:
            self.producer.begin_transaction()
            self._active_transaction = True
        produce_message(self.producer, producer_kwargs, self.metrics_manager, self.headers())
        self.producer.poll(0)

    def commit(self, mark_committed=True):
        if self._active_transaction:
            self.producer.send_offsets_to_transaction(
                [TopicPartition(self.topic(), self.partition(), self.offset() + 1)], self.consumer.consumer_group_metadata())
            self.producer.commit_transaction()
            self.producer.poll(0)
            self._committed = mark_committed


class TransactionApp:
    def __init__(self, app_function, consume_topics_list, produce_topic_schema_dict, 
                 metrics_manager=None, schema_registry=None, cluster=None, consumer=None, producer=None):
        self.app_function = app_function
        self.metrics_manager = metrics_manager
        if not schema_registry:
            self.schema_registry = init_schema_registry_configs(as_registry_object=True)
        if not consumer:
            self.consumer = get_transactional_consumer(consume_topics_list, self.schema_registry, cluster=cluster)
        if not producer:
            self.producer = get_transactional_producer(produce_topic_schema_dict, self.schema_registry, cluster=cluster)

    def consume(self, timeout=None):
        return consume_message(self.consumer, self.metrics_manager, timeout)

    def run(self, *args, **kwargs):
        try:
            while True:
                transaction = None
                try:
                    transaction = Transaction(self.consume(), self.producer, self.consumer, self.metrics_manager)
                    self.app_function(transaction, *args, **kwargs)
                    if not transaction._committed:
                        transaction.commit()
                except NoMessageError:
                    self.producer.poll(0)
                except Exception as e:
                    raise
        finally:
            # TODO: might need to move the transaction abort within the while loop. 
            if transaction:
                if transaction._active_transaction:
                    self.producer.abort_transaction(10)
            shutdown_cleanup(consumer=self.consumer)


class TableTransaction(Transaction):
    def __init__(self, message, producer, consumer, metrics_manager, changelog_topic, rdb_tables):
        self.message = message
        self.changelog_topic = changelog_topic
        self.rdb_tables = rdb_tables

        self._changelog_updated = False
        self._pending_table_write = None

        super().__init__(self.message, producer, consumer, metrics_manager)

    def read_table_entry(self):
        return self._rdb_read()

    def update_table_entry(self, value):
        self._pending_table_write = deepcopy(value)
        if isinstance(self._pending_table_write, (list, dict)):
            # LOGGER.debug(f'attempting json dumps of {self._pending_table_write}')
            self._pending_table_write = dumps(self._pending_table_write)

    def delete_table_entry(self):
        self._pending_table_write = '-DELETED-'

    def _update_changelog(self):
        self.produce(dict(
            topic=self.changelog_topic,
            key=self.key(),
            value=self._pending_table_write
        ))
        self._changelog_updated = True
        self.producer.poll(0)

    def _recover_table_via_changelog(self):
        value = self.value()
        try:
            value = loads(value)
        except:
            pass
        if value == '-DELETED-':
            self.delete_table_entry()
        else:
            self.update_table_entry(value)
        super().commit()
        self._rdb_write(self._pending_table_write)

    def _rdb_write(self, value):
        if self._pending_table_write == '-DELETED-':
            LOGGER.debug('Finalizing table entry delete...')
            self.rdb_tables[self.partition()].delete(self.key())
            self.rdb_tables[self.partition()].write('offset', str(self._rdb_offset() + 2))
        else:
            # LOGGER.debug(f'Finalizing table entry write:\npartition{self.partition()},\nkey:{self.key()},\nvalue:{self._pending_table_write}...')
            LOGGER.debug(f'Finalizing table entry write:\npartition{self.partition()},\nkey:{self.key()}')
            self.rdb_tables[self.partition()].write_batch(
                {self.key(): self._pending_table_write,
                 'offset': str(self._rdb_offset() + 2)})
        self._pending_table_write = None

    def _rdb_read(self):
        value = self.rdb_tables[self.partition()].read(self.key())
        try:
            value = loads(value)
        except:
            pass
        LOGGER.debug(f'Read table value: {value}')
        return value

    def _rdb_offset(self):
        value = self.rdb_tables[self.partition()].read('offset')
        if not value:
            value = self.offset() if self.offset() else 0
        return int(value)

    def commit(self):
        if not self._changelog_updated and self._pending_table_write:
            self._update_changelog()
        super().commit(mark_committed=False)
        if self._pending_table_write:
            self._rdb_write(self._pending_table_write)


class TableApp(TransactionApp):
    def __init__(self, app_function, consume_topics_list, produce_topic_schema_dict, 
                 metrics_manager=None, schema_registry=None, cluster=None, consumer=None, producer=None):
        self.changelog_topic = f"{environ['APP_NAME']}__changelog"
        if self.changelog_topic not in produce_topic_schema_dict:
            produce_topic_schema_dict.update({self.changelog_topic: changelog_schema})
        self.topic = consume_topics_list
        self.rdb_tables = {}
        self._pending_primary_partitions = {}
        self._pending_table_recoveries = {}
        if not schema_registry:
            self.schema_registry = init_schema_registry_configs(as_registry_object=True)
        if not consumer:
            self.consumer = self._set_table_consumer(self.topic, self.schema_registry, cluster=cluster)
        super().__init__(
            app_function, consume_topics_list, produce_topic_schema_dict,
            metrics_manager=metrics_manager, schema_registry=schema_registry, cluster=cluster, consumer=self.consumer, producer=producer)

    def _rdb_close(self, partitions=None):
        full_shutdown = False
        if not partitions:
            partitions = list(self.rdb_tables.keys())
            full_shutdown = True
        LOGGER.debug(f'RocksDB - closing connections for partitions {partitions}')
        for p in partitions:
            try:
                self.rdb_tables[p].close()
                del self.rdb_tables[p]
                LOGGER.debug(f'p{p} RDB table connection closed.')
            except KeyError:
                if not full_shutdown:
                    LOGGER.debug(
                        f'RDB Table p{p} did not seem to be mounted and thus could not unmount,'
                        f' likely caused by multiple rebalances in quick succession.'
                        f' This is unliklely to cause issues as the client is in the middle of adjusting itself, '
                        f' but should be noted.')
        LOGGER.info(f'RocksDB - closed connections for partitions {partitions}')

    def _confirm_proper_assignment(self):
        assignments = self.consumer.assignment()
        if self.changelog_topic in [p_obj.topic for p_obj in assignments]:
            raise Exception('changelog topic was included in normal consumption assignment! ABANDON SHIP!!!')
        topic = set([p_obj.partition for p_obj in assignments])
        tables = set(self.rdb_tables)
        if topic != tables:
            LOGGER.warning(f"Partition/Table assignment mismatch!! topic: {topic}; tables: {tables}")

    def _resume_consumption(self, from_recovery=False):
        if from_recovery:
            changelog_unassign = [p_obj for p_obj in self.consumer.assignment() if p_obj.topic == self.changelog_topic]
            LOGGER.debug(f'unassigning changelog partitions: {changelog_unassign}')
            self.consumer.incremental_unassign(changelog_unassign)
            LOGGER.debug(f'Resuming consumption for partitions:\n{list(self._pending_primary_partitions.values())}')
            self.consumer.resume(list(self._pending_primary_partitions.values()))
        self._confirm_proper_assignment()
        self._pending_table_recoveries = {}
        self._pending_primary_partitions = {}
        LOGGER.info('Continuing normal consumption loop...')

    def _rdb_init(self, partition):
        self.rdb_tables[partition] = RDB(f'p{partition}')
        LOGGER.debug(f'RDB table for p{partition} initialized')

    def _get_changelog_watermarks(self, recovery_partitions):
        """
        Note: this is a separate function since it requires the consumer to communicate with the broker
        """
        return {p: self.consumer.get_watermark_offsets(p_obj) for p, p_obj in recovery_partitions.items()}

    def _refresh_pending_table_recoveries(self):
        """
        confirms new recoveries and removes old ones if not applicable anymore
        """
        recovery_partitions = {p: TopicPartition(topic=self.changelog_topic, partition=p) for p, p_obj in
                                             self._pending_primary_partitions.items()}
        tables_to_recover = {}
        for partition, watermarks in self._get_changelog_watermarks(recovery_partitions).items():
            LOGGER.debug(f'(lowwater, highwater) for changelog p{partition}: {watermarks}')
            if watermarks[0] != watermarks[1]:
                table_offset = self.rdb_tables[partition].read('offset')
                if table_offset:
                    table_offset = int(table_offset)
                else:
                    table_offset = 0
                if table_offset < watermarks[1]:
                    tables_to_recover[partition] = {'table_offset': table_offset, 'watermarks': watermarks, 'partition_obj': recovery_partitions[partition]}
        self._pending_table_recoveries = tables_to_recover

    def _init_rdb_tables(self, partition_objs):
        for p in partition_objs:
            partition = p.partition
            if partition not in self.rdb_tables:
                self._rdb_init(partition)

    def _new_table_recoveries(self, new_partitions):
        self._refresh_pending_table_recoveries()
        return {p: table_meta for p, table_meta in self._pending_table_recoveries.items() if p in new_partitions}

    def _recover_or_resume(self):
        # TODO: check to see if handling it via exception is actually necessary anymore?
        """
        Due to confluent-kafka consumers asynchronous operations, the best way to force a desired
        control flow within the general app consumer loop is to raise an exception and
        interrupt whatever the app is currently doing and start recovering.
        """
        if self._pending_table_recoveries:
            LOGGER.debug(f'Table recovery required: {self._pending_table_recoveries}')
            raise RunTableRecovery
        else:
            LOGGER.debug('Preparing to resume consumption pattern...')
            self._resume_consumption()

    def _rocksdb_assign(self, consumer, add_partition_objs):
        """
        NOTE: confluent-kafka expects this method to have exactly these two arguments ONLY
        NOTE: _rocksdb_assign will ALWAYS be called (even when no new assignments are required) after _rocksdb_unassign.
        """
        LOGGER.info('Rebalance Triggered - Assigment')
        LOGGER.debug(f'Consumer - Assigning additional partitions: {[p_obj.partition for p_obj in add_partition_objs]}')
        if add_partition_objs:
            new_partitions = {p_obj.partition: p_obj for p_obj in add_partition_objs}
            self._pending_primary_partitions.update(new_partitions)
            self._init_rdb_tables(list(self._pending_primary_partitions.values()))
            add_table_recovery = self._new_table_recoveries(new_partitions)
            self.consumer.incremental_assign(add_partition_objs)
            if add_table_recovery:
                LOGGER.debug('New partition assignment will require table recovery...')
                self.consumer.incremental_assign([v['partition_obj'] for k, v in self._pending_table_recoveries.items() if k in new_partitions])  # could do all of them, but less exception handling/cleaner this way
        else:
            has_assignments = self.consumer.assignment()
            if has_assignments:
                LOGGER.debug('No new/additional partitions assigned.')
                LOGGER.info(f'Resuming current assignment of: {[p_obj.partition for p_obj in has_assignments]}')
            else:
                LOGGER.info('Awaiting partition assignments from broker...')
        LOGGER.info('Consumer - Assignment request complete.')
        self._recover_or_resume()

    def _rocksdb_unassign(self, consumer, drop_partition_objs):
        """
        NOTE: confluent-kafka expects this method to have exactly these two arguments ONLY
        NOTE: _rocksdb_assign will always be called (even when no new assignments are required) after _rocksdb_unassign.
        """
        partitions = [p_obj.partition for p_obj in drop_partition_objs]
        LOGGER.debug(f'Consumer - Unassigning topic {self.topic} partitions: {partitions}')
        self.consumer.incremental_unassign(drop_partition_objs)
        if self._pending_table_recoveries:
            self.consumer.incremental_assign([v['partition_obj'] for k, v in self._pending_table_recoveries.items() if k in drop_partition_objs])
        self._pending_primary_partitions = {k: v for k, v in self._pending_primary_partitions.items() if
                                               k not in partitions}
        self._pending_table_recoveries = {k: v for k, v in self._pending_table_recoveries.items() if
                                          k not in partitions}
        LOGGER.debug(f'pending_primary_partitions after unassignment: {self._pending_primary_partitions}')
        LOGGER.debug(f'table_recovery_status after unassignment: {self._pending_table_recoveries}')
        self._rdb_close(partitions)

    def _set_table_consumer(self, topic, schema_registry, default_schema=None, cluster=None):
        consumer = get_transactional_consumer(topic, schema_registry, default_schema, False, cluster)
        consumer.subscribe([topic], on_assign=self._rocksdb_assign, on_revoke=self._rocksdb_unassign, on_lost=self._rocksdb_unassign)
        LOGGER.debug('Table consumer initialized')
        return consumer

    def _table_recovery_refresh_starting_offsets(self):
        for p, offsets in self._pending_table_recoveries.items():
            new_offset = self._pending_table_recoveries[p]['table_offset']
            low_mark = self._pending_table_recoveries[p]['watermarks'][0]
            if low_mark > new_offset:  # handles offsets that have been removed/compacted. Should never happen, but ya know
                LOGGER.info(
                    f'p{p} table has an offset ({new_offset}) less than the changelog lowwater ({low_mark}), likely due to retention settings. Setting {low_mark} as offset start point.')
                new_offset = low_mark
            high_mark = self._pending_table_recoveries[p]['watermarks'][1]
            LOGGER.debug(f'p{p} table has an offset delta of {high_mark - new_offset}')
            self._pending_table_recoveries[p]['partition_obj'].offset = new_offset

    def _table_recovery_loop(self, checks=3):
        LOGGER.info('BEGINNING TABLE RECOVERY PROCEDURE')
        while checks and self._pending_table_recoveries:
            try:
                transaction = TableTransaction(self.consume(timeout=3), self.producer, self.consumer,
                                               self.metrics_manager,
                                               self.changelog_topic, self.rdb_tables)
                LOGGER.debug(f'Recovery write is {transaction.value()}')
                transaction._recover_table_via_changelog()
                p = transaction.partition()
                LOGGER.debug(
                    f"transaction_offset - {transaction.offset() + 2}, watermark - {self._pending_table_recoveries[p]['watermarks'][1]}")
                if self._pending_table_recoveries[p]['watermarks'][1] - (transaction.offset() + 2) <= 0:
                    LOGGER.info(f'table partition {p} fully recovered!')
                    del self._pending_table_recoveries[p]
            except NoMessageError:
                checks -= 1
                LOGGER.debug(f'No changelog messages, checks remaining: {checks_left}')
        LOGGER.info("TABLE RECOVERY COMPLETE!")

    def _throwaway_poll(self):
        LOGGER.debug("Performing throwaway poll to allow assignments to properly initialize...")
        try:
            TableTransaction(self.consume(timeout=3), self.producer, self.consumer, self.metrics_manager,
                             self.changelog_topic, self.rdb_tables)
        except NoMessageError:
            pass

    def _table_recovery(self):
        # TODO: check if this is necc (maybe if you don't do an exception interrupt?
        # while self._pending_table_recoveries: # In case of rebalance interruptions
        try:
            self._table_recovery_refresh_starting_offsets()
            LOGGER.debug(f'table_recovery_status before recovery attempt: {self._pending_table_recoveries}')
            for table_meta in self._pending_table_recoveries.values():
                self.consumer.seek(table_meta['partition_obj'])
            self._table_recovery_loop()
            self._resume_consumption(from_recovery=True)
        except KafkaException as e:
            if 'Failed to seek to offset' in e.args[0].str():
                LOGGER.debug('Running a consumer poll to allow seeking to work on the changelog partitions...')
                self._throwaway_poll()
                self._table_recovery()
        except Exception as e:
            LOGGER.debug(f'{[arg for arg in e.args]}')
            LOGGER.debug('Table recovery interrupted due to rebalance...retrying')

    def run(self, *args, **kwargs):
        transaction = None
        try:
            while True:
                try:
                    transaction = TableTransaction(self.consume(), self.producer, self.consumer, self.metrics_manager, self.changelog_topic, self.rdb_tables)
                    self.app_function(transaction, *args, **kwargs)
                    if not transaction._committed:
                        transaction.commit()
                except NoMessageError:
                    self.producer.poll(0)
                    LOGGER.debug('No messages!')
                except RunTableRecovery:
                    self._table_recovery()
                except Exception as e:
                    raise
        finally:
            LOGGER.info('App is shutting down...')
            try:
                if transaction._active_transaction:
                    self.producer.abort_transaction(10)
            except:
                pass
            finally:
                shutdown_cleanup(consumer=self.consumer)
                self._rdb_close()
