# Copyright (c) Qotto, 2021

from __future__ import annotations

import logging
import threading
import time
from threading import Thread
from typing import Optional, Iterable, Callable
from uuid import uuid4

from eventy.messaging.agent import Agent, Handler, Guarantee
from eventy.messaging.errors import AppCancelled, ParentThreadDied, BatchFailed, EventyAppInterrupted, MessagingError
from eventy.messaging.service import Service
from eventy.messaging.store import Cursor, RecordStore, RecordWriteStore, RecordStoreWithInitialization
from eventy.record import Record, Response, RecordType
from eventy.trace_id.local import local_trace

__all__ = [
    'EventyApp',
]

logger = logging.getLogger(__name__)


class EventyApp:
    """
    EventyApp is the messaging application.
    """

    def __init__(
        self,
        record_store: RecordStore,
        app_service: Service,
        ext_services: Iterable[Service] = None,
        agents: Iterable[Agent] = None,
        handlers: Iterable[Handler] = None,
        read_batch_size: int = 1,
        read_timeout_ms: Optional[int] = None,
        read_wait_time_ms: Optional[int] = None,
        write_timeout_ms: Optional[int] = None,
        ack_timeout_ms: Optional[int] = None,
        commit_timeout_ms: Optional[int] = None,
    ):
        self._record_store = record_store
        self._app_service = app_service
        self._ext_services = ext_services or []
        self._all_handlers = list()
        if handlers is not None:
            for handler in handlers:
                self._all_handlers.append(handler)
        if agents is not None:
            for agent in agents:
                for handler in agent.handlers:
                    self._all_handlers.append(handler)

        self._read_batch_size = read_batch_size
        self._read_timeout_ms = read_timeout_ms
        self._write_timeout_ms = write_timeout_ms
        self._ack_timeout_ms = ack_timeout_ms
        self._commit_timeout_ms = commit_timeout_ms
        self._read_wait_time_ms = read_wait_time_ms or 0

        self._write_store = _AppRecordWriteStore(self)
        self._started = False
        self._cancelled = False
        self._process_thread: Optional[Thread] = None
        self._error: Optional[MessagingError] = None

    def _get_service_for_name(self, service_name: Optional[str]):
        if service_name is None:
            return self._app_service
        for service in self._ext_services:
            if service.name == service_name:
                return service
        raise ValueError(f"Service {service_name} not found.")

    def _get_topics_to_register(self) -> list[str]:
        topics: set[str] = set()
        for handler in self._all_handlers:
            service = self._get_service_for_name(handler.service_name)
            topic = service.topic_for(handler.record_type)
            logger.info(f"Found handler {handler}. Will listen topic {topic}.")
            topics.add(topic)
        return list(sorted(topics))

    def _get_handlers_for_record(self, record: Record, guarantee: Guarantee) -> list[Handler]:
        handlers: list[Handler] = list()
        for handler in self._all_handlers:
            if (
                handler.record_type == record.type
                and handler.record_name == record.name
                and handler.delivery_guarantee == guarantee
                and self._get_service_for_name(handler.service_name).namespace == record.namespace
            ):
                if isinstance(record, Response):
                    if record.destination == self._app_service.namespace:
                        handlers.append(handler)
                else:
                    handlers.append(handler)
        return handlers

    def _get_topic_for_record(self, record: Record) -> str:
        if record.type == RecordType.EVENT or record.type == RecordType.RESPONSE:
            return self._app_service.topic_for(record.type)
        for service in self._ext_services:
            if service.namespace == record.namespace:
                return service.topic_for(record.type)
        raise ValueError(f"No topic for record {record}.")

    @property
    def is_alive(self) -> bool:
        return bool(self._process_thread and self._process_thread.is_alive())

    @property
    def get_error(self) -> Optional[MessagingError]:
        return self._error

    @property
    def write_store(self) -> RecordWriteStore:
        return self._write_store

    def _process_one_record_one_handler(self, record: Record, handler: Handler) -> None:
        logger.debug(
            f"Processing record {record.qualified_name} data={record.data} with handler {handler}."
        )
        for output_record in handler.handle_record(record):
            topic = self._get_topic_for_record(output_record)
            logger.debug(
                f"Writing output record {record.qualified_name} on topic {topic} with data={record.data}."
            )
            self._record_store.write(output_record, topic, self._write_timeout_ms, )

    def _process_one_batch(self) -> None:
        records = list(
            self._record_store.read(
                max_count=self._read_batch_size,
                timeout_ms=self._read_timeout_ms,
                auto_ack=False,
            )
        )
        if records:
            logger.debug(f"Received {len(records)} new records.")
        else:
            time.sleep(self._read_wait_time_ms / 1000)
            return

        # At Least Once
        for record in records:
            with local_trace(correlation_id=record.correlation_id):
                for handler in self._get_handlers_for_record(record, Guarantee.AT_LEAST_ONCE):
                    self._process_one_record_one_handler(record, handler)

        # Exactly Once
        self._record_store.start_transaction()
        self._record_store.ack(self._ack_timeout_ms)
        for record in records:
            with local_trace(correlation_id=record.correlation_id):
                for handler in self._get_handlers_for_record(record, Guarantee.EXACTLY_ONCE):
                    self._process_one_record_one_handler(record, handler)
        self._record_store.commit(self._commit_timeout_ms)

        # At Most Once
        for record in records:
            with local_trace(correlation_id=record.correlation_id):
                for handler in self._get_handlers_for_record(record, Guarantee.AT_MOST_ONCE):
                    self._process_one_record_one_handler(record, handler)

    def run(
        self,
        keep_alive=False,
        on_interrupted: Optional[Callable[[], None]] = None,
    ) -> None:
        """
        Run in a separate thread.

        :param keep_alive: If True, the app will not exit until the calling thread is finished.
        :param on_interrupted: Callback to be called when the thread is interrupted.
        """
        logger.info(f"Starting Eventy App <{self._app_service.name}>.")

        topics_to_register = self._get_topics_to_register()
        logger.info(
            f"Starting Eventy App <{self._app_service.name}>: "
            f"registering {len(topics_to_register)} topics: {', '.join(topics_to_register)}."
        )
        for topic in topics_to_register:
            logger.debug(f"Will register to topic: {topic}.")
            try:
                self._record_store.register_topic(topic, Cursor.ACKNOWLEDGED)
            except Exception as e:
                logger.error(f"Failed to register to topic {topic}: {e}")

        if isinstance(self._record_store, RecordStoreWithInitialization):
            logger.info(f"Starting Eventy App <{self._app_service.name}>. Store needs initialization.")
            self._record_store.initialize()

        if topics_to_register:
            logger.info(f"Starting Eventy App <{self._app_service.name}>. Will now start the process loop.")
        else:
            # We can skip processing records if there is no topic to read from.
            logger.warning(
                f"Starting Eventy App <{self._app_service.name}>: "
                f"Will not start processing loop (no topics to read)."
            )
            return

        current_thread = threading.current_thread()

        def run_loop():
            while True:
                try:
                    if self._cancelled:
                        raise AppCancelled
                    elif not keep_alive and not current_thread.is_alive():
                        raise ParentThreadDied
                    else:
                        try:
                            self._process_one_batch()
                        except Exception as batch_error:
                            logger.exception(
                                f"Failed to process batch in {self._app_service.name}. Will terminate App."
                            )
                            raise BatchFailed(
                                f"Failed to process batch in {self._app_service.name}."
                            ) from batch_error
                except EventyAppInterrupted as interruption_error:
                    self._error = interruption_error
                    logger.warning(f"Stopped processing records <{self._app_service.name}>. Reason: {self._error}.")
                    break

            if on_interrupted:
                on_interrupted()

        self._process_thread = Thread(
            name=f"App-Process-{uuid4().hex[-6:]}",
            target=run_loop,
        )

        logger.info(f"Starting Eventy App <{self._app_service.name}>: starting processing thread.")
        self._process_thread.start()
        self._started = True

        logger.info(f"Starting Eventy App <{self._app_service.name}>: started.")

    def cancel(self) -> None:
        if self._started and not self._cancelled:
            logger.info(f"Waiting process thread to join if necessary.")
            self._cancelled = True
            if self._process_thread and self._process_thread.is_alive():
                self._process_thread.join()

    def __del__(self):
        self.cancel()


class _AppRecordWriteStore(RecordWriteStore):
    def __init__(self, app: EventyApp):
        self._app = app

    def write(self, record: Record) -> None:
        with local_trace(correlation_id=record.correlation_id):
            topic = self._app._get_topic_for_record(record)
            logger.debug(f"Writing record {record.qualified_name} data={record.data} to topic: {topic}.")
            self._app._record_store.write_now(
                record,
                topic,
                self._app._write_timeout_ms,
            )
