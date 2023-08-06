# Copyright (c) Qotto, 2021

from __future__ import annotations

import logging
import socket
import threading
import time
from concurrent.futures import Future
from threading import Thread, Lock
from time import sleep
from typing import Iterable, Optional
from uuid import uuid4

from confluent_kafka import Producer, Consumer, Message, TopicPartition

from eventy.config import SERVICE_NAME
from eventy.messaging.errors import MessagingError
from eventy.messaging.store import Cursor, RecordStoreWithInitialization
from eventy.record import Record
from eventy.serialization import RecordSerializer

__all__ = [
    'CKStore',
]

from eventy.trace_id import local_trace

logger = logging.getLogger(__name__)


def _message_str(message: Message) -> str:
    return f'{message.topic()}[{message.partition()}]:{message.offset()}'


def _partitions_str(partitions: list[TopicPartition]) -> str:
    partitions_dict = {}
    for partition in partitions:
        if partition.topic not in partitions_dict:
            partitions_dict[partition.topic] = [partition.partition]
        else:
            partitions_dict[partition.topic].append(partition.partition)
    partitions_summary_str = ', '.join([f'{topic}{parts}' for topic, parts in partitions_dict.items()])
    partitions_complete_str = ', '.join(f'{p.topic}[{p.partition}]:{p.offset} (err:{p.error})' for p in partitions)
    return f'{partitions_summary_str}\n{partitions_complete_str}'


def _on_assign(consumer: Consumer, partitions: list[TopicPartition]) -> None:
    partitions_str = _partitions_str(partitions)
    logger.info(f"Kafka Subscribe: ASSIGNED partitions for consumer {consumer}: " + partitions_str)


def _on_revoke(consumer: Consumer, partitions: list[TopicPartition]) -> None:
    partitions_str = _partitions_str(partitions)
    logger.info(f"Kafka Subscribe: REVOKED partitions for consumer {consumer}: " + partitions_str)


def _on_lost(consumer: Consumer, partitions: list[TopicPartition]) -> None:
    partitions_str = _partitions_str(partitions)
    logger.info(f"Kafka Subscribe: LOST partitions for consumer {consumer}: " + partitions_str)


class CKStore(RecordStoreWithInitialization):
    """
    Kafka implementation of a record store, using Confluent kafka library
    """

    transactional_producer: Producer
    immediate_producer: Producer
    consumer: Consumer
    poll_thread: Thread

    def __init__(
        self,
        serializer: RecordSerializer,
        bootstrap_servers: list[str],
        group_id: Optional[str] = None,
        transactional_id: Optional[str] = None,
        sasl_username: Optional[str] = None,
        sasl_password: Optional[str] = None,
    ) -> None:
        """
        Initialize the store

        :param serializer: Record serializer (read and write)
        :param bootstrap_servers: Kafka bootstrap servers (producer and consumer)
        :param group_id: Kafka group id (consumer), default: service name
        :param transactional_id: Kafka transactional id (producer), default: to unique id
        :param sasl_username: Optional username (if SASL PLAIN kafka connection, producer and consumer)
        :param sasl_password: Optional password (if SASL PLAIN kafka connection, producer and consumer)
        """
        # Initialize topics to register
        super().__init__()
        # Kafka config
        self.serializer = serializer
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id or SERVICE_NAME
        self.transactional_id = transactional_id or f'{SERVICE_NAME}-{str(uuid4())}'
        self.sasl_username = sasl_username
        self.sasl_password = sasl_password
        # Other attributes
        self.initialized = False
        self.in_transaction = False
        self.cancelled = False
        self.initialization_lock = Lock()

    def initialize(self) -> None:
        self._check_initialized()

    def register_topic(self, topic: str, cursor: Cursor = Cursor.ACKNOWLEDGED):
        if cursor != Cursor.ACKNOWLEDGED:
            raise NotImplementedError(f"Only {Cursor.ACKNOWLEDGED} implemented for now.")
        super().register_topic(topic, cursor)
        logger.info(f"Registered topic {topic}: {cursor}.")

    def _check_initialized(self) -> None:
        with self.initialization_lock:
            if self.initialized:
                logger.debug("Kafka store already initialized.")
                return

            logger.info(f"Will initialize Kafka producer and consumer.")

            # configs
            transactional_producer_config = {
                'bootstrap.servers': ','.join(self.bootstrap_servers),
                'transactional.id': self.transactional_id,
                'client.id': socket.gethostname(),
            }
            immediate_producer_config = {
                'bootstrap.servers': ','.join(self.bootstrap_servers),
                'client.id': socket.gethostname(),
                'enable.idempotence': 'true',
            }
            consumer_config = {
                'bootstrap.servers': ','.join(self.bootstrap_servers),
                'group.id': self.group_id,
                'client.id': socket.gethostname(),
                'enable.auto.commit': 'false',
                'auto.offset.reset': 'earliest',
                'isolation.level': 'read_committed',
            }

            # SASL authentication
            if self.sasl_username and self.sasl_password:
                for config in [
                    transactional_producer_config,
                    immediate_producer_config,
                    consumer_config,
                ]:
                    config.update(
                        {
                            'sasl_mechanism': 'PLAIN',
                            'sasl_plain_username': self.sasl_username,
                            'sasl_plain_password': self.sasl_password,
                        }
                    )

            # producers
            logger.info(f"Initializing transactional Kafka producer with config {transactional_producer_config}.")
            self.transactional_producer = Producer(transactional_producer_config)
            self.transactional_producer.init_transactions()
            logger.debug(f"Initialized transactional Kafka producer.")

            logger.info(f"Initializing immediate Kafka producer with config {immediate_producer_config}.")
            self.immediate_producer = Producer(immediate_producer_config)
            logger.debug(f"Initialized immediate Kafka producer.")

            # consumer
            consumer_topics = [topic for topic in self.topics]
            logger.info(f"Initializing Kafka consumer with config {consumer_config} and topics {consumer_topics}.")
            self.consumer = Consumer(consumer_config)
            if consumer_topics:
                self.consumer.subscribe(
                    consumer_topics,
                    on_assign=_on_assign,
                    on_revoke=_on_revoke,
                    on_lost=_on_lost,
                )
            logger.debug(f"Initialized Kafka consumer.")

            # poll loop
            current_thread = threading.current_thread()

            def poll_loop():

                while True:
                    if self.cancelled:
                        finish_reason = "cancelled"
                        break
                    elif not current_thread.is_alive():
                        finish_reason = "parent thread not alive"
                        break
                    else:
                        try:
                            immediate_polled = self.immediate_producer.poll(0.005)
                            if immediate_polled:
                                logger.debug(f"Immediate producer polled {immediate_polled} messages.")
                            transactional_polled = self.transactional_producer.poll(0.005)
                            if transactional_polled:
                                logger.debug(f"Transactional producer polled {transactional_polled} messages.")
                        except Exception as e:
                            logger.warning(f"Kafka exception in poll loop: {e}")
                            sleep(30)
                logger.warning(f"Kafka poll loop stopped. Reason: {finish_reason}.")

            self.poll_thread = Thread(
                name=f"CK-Poll-{uuid4().hex[-6:]}",
                target=poll_loop,
            )

            logger.debug(f"Will start Kafka poll loop thread.")
            self.poll_thread.start()

            self.initialized = True
            logger.debug(f"Record Store initialized.")

    def read(
        self,
        max_count: int = 1, timeout_ms: Optional[int] = None, auto_ack: bool = False
    ) -> Iterable[Record]:
        """
        Reads records from kafka.

        :raise MessagingError: if there is an error reading from kafka.

        :param max_count:
        :param timeout_ms:
        :param auto_ack:
        :return:
        """
        self._check_initialized()

        if not self.topics:
            logger.debug(f"No topics configured. Returning empty list.")
            return []

        try:
            partitions_str = _partitions_str(self.consumer.assignment())
            logger.debug(f"Reading at most {max_count} records from Kafka. Current assignment is {partitions_str}.")
            messages: list[Message] = self.consumer.consume(max_count, _ms2sec(timeout_ms))
            logger.debug(f"Read {len(messages)} messages from Kafka.")
        except Exception:
            raise MessagingError(f"Error consuming messages from kafka.")

        for message in messages:
            if message.error():
                logger.error(
                    f"Message {_message_str(message)} has error {message.error()}."
                )
                continue
            logger.debug(f"New message {_message_str(message)}.")
            try:
                # noinspection PyArgumentList
                # PyCharm is wrong, there is no payload arg
                encoded = message.value()
                record = self.serializer.decode(encoded)
            except Exception as e:
                raise MessagingError(f"Error decoding message {_message_str(message)}.") from e
            with local_trace(correlation_id=record.correlation_id):
                logger.info(
                    f"New record {record.qualified_name} from kafka message {_message_str(message)}."
                )
            yield record
            if auto_ack:
                try:
                    self.consumer.commit(message=message, asynchronous=False)
                except Exception:
                    raise MessagingError(
                        f"Error committing message {_message_str(message)}."
                    )

    def ack(self, timeout_ms=None) -> None:
        self._check_initialized()

        if self.in_transaction:
            logger.info(f"Ack read messages in transaction (will send offsets to transaction).")
            try:
                self.transactional_producer.send_offsets_to_transaction(
                    self.consumer.position(self.consumer.assignment()),
                    self.consumer.consumer_group_metadata(),
                    _ms2sec(timeout_ms)
                )
            except Exception:
                raise MessagingError(f"Error sending offsets to transaction.")
        else:
            logger.info(f"Ack read messages outside transaction.")
            try:
                self.consumer.commit(asynchronous=False)
            except Exception as e:
                raise MessagingError(f"Error committing message.") from e

    def _write(self, producer: Producer, record: Record, topic: str, timeout_ms=None) -> None:

        # handle callback
        future_result: Future = Future()

        def ack(err, msg):
            with local_trace(correlation_id=record.correlation_id):
                if err:
                    logger.debug(f"Produced with errors: {err}.")
                    future_result.set_exception(MessagingError(err))
                else:
                    logger.debug(f"Produced successfully.")
                    future_result.set_result(msg)

        # produce message
        logger.debug(f"Will produce record {record.qualified_name} on {topic}.")
        producer.produce(
            topic=topic,
            value=self.serializer.encode(record),
            key=record.partition_key,
            on_delivery=ack
        )

        # wait callback
        total_time_ms = 0.0
        while not future_result.done():
            time_ms = 1 + total_time_ms / 10
            time.sleep(time_ms / 1000)  # in secs
            total_time_ms = total_time_ms + time_ms
            if timeout_ms is not None and total_time_ms > timeout_ms:
                raise TimeoutError(f"Write timed out {int(total_time_ms)} ms.")

        # handle exceptions
        exception = future_result.exception()
        if exception:
            raise MessagingError(exception)

        # handle interrupted thread
        result = future_result.result()
        if not result:
            raise MessagingError(f"Could not write. Was the thread was interrupted?")

    def write(self, record: Record, topic: str, timeout_ms=None) -> None:
        self._check_initialized()

        if self.in_transaction:
            self._write(self.transactional_producer, record, topic, timeout_ms)
        else:
            self._write(self.immediate_producer, record, topic, timeout_ms)

    def write_now(self, record: Record, topic: str, timeout_ms=None) -> None:
        self._check_initialized()

        self._write(self.immediate_producer, record, topic, timeout_ms)

    def start_transaction(self) -> None:
        self._check_initialized()

        if self.in_transaction:
            raise MessagingError(f"Already in a transaction.")
        self.transactional_producer.begin_transaction()
        self.in_transaction = True

    def commit(self, timeout_ms: Optional[int] = None) -> None:
        self._check_initialized()

        if not self.in_transaction:
            raise MessagingError(f"Not in a transaction.")
        self.transactional_producer.commit_transaction(_ms2sec(timeout_ms))
        logger.info(f"Committed transaction.")
        self.in_transaction = False

    def abort(self, timeout_ms: Optional[int] = None) -> None:
        self._check_initialized()

        if not self.in_transaction:
            raise MessagingError(f"Not in a transaction.")
        self.transactional_producer.abort_transaction(_ms2sec(timeout_ms))
        logger.info(f"Aborted transaction.")
        self.in_transaction = False

    def __del__(self):
        if self.initialized:
            logger.info(f"Waiting poll thread to join.")
            self.cancelled = True
            self.poll_thread.join()
            logger.info(f"Poll thread joined.")


def _ms2sec(timeout_ms: Optional[int]) -> float:
    timeout_sec = -1.0
    if timeout_ms:
        timeout_sec = timeout_ms / 1000
    return timeout_sec
