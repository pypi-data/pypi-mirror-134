import zlib
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from unittest import TestCase
from uuid import uuid4

from eventsourcing.cipher import AESCipher
from eventsourcing.compressor import ZlibCompressor
from eventsourcing.domain import TZINFO, DomainEvent
from eventsourcing.persistence import (
    AggregateRecorder,
    ApplicationRecorder,
    DatetimeAsISO,
    DecimalAsStr,
    InfrastructureFactory,
    JSONTranscoder,
    Mapper,
    ProcessRecorder,
    UUIDAsHex,
)
from eventsourcing.utils import Environment, get_topic


class InfrastructureFactoryTestCase(ABC, TestCase):
    env: Optional[Environment] = None

    @abstractmethod
    def expected_factory_class(self):
        pass

    @abstractmethod
    def expected_aggregate_recorder_class(self):
        pass

    @abstractmethod
    def expected_application_recorder_class(self):
        pass

    @abstractmethod
    def expected_process_recorder_class(self):
        pass

    def setUp(self) -> None:
        self.factory = InfrastructureFactory.construct(self.env)
        self.assertIsInstance(self.factory, self.expected_factory_class())
        self.transcoder = JSONTranscoder()
        self.transcoder.register(UUIDAsHex())
        self.transcoder.register(DecimalAsStr())
        self.transcoder.register(DatetimeAsISO())

    def test_createmapper(self):

        # Want to construct:
        #  - application recorder
        #  - snapshot recorder
        #  - mapper
        #  - event store
        #  - snapshot store

        # Want to make configurable:
        #  - cipher (and cipher key)
        #  - compressor
        #  - application recorder class (and db uri, and session)
        #  - snapshot recorder class (and db uri, and session)

        # Common environment:
        #  - factory topic
        #  - cipher topic
        #  - cipher key
        #  - compressor topic

        # POPO environment:

        # SQLite environment:
        #  - database topic
        #  - table name for stored events
        #  - table name for snapshots

        # Create mapper.

        mapper = self.factory.mapper(
            transcoder=self.transcoder,
        )
        self.assertIsInstance(mapper, Mapper)
        self.assertIsNone(mapper.cipher)
        self.assertIsNone(mapper.compressor)

    def test_createmapper_with_compressor(self):

        # Create mapper with compressor class as topic.
        self.env[self.factory.COMPRESSOR_TOPIC] = get_topic(ZlibCompressor)
        mapper = self.factory.mapper(transcoder=self.transcoder)
        self.assertIsInstance(mapper, Mapper)
        self.assertIsInstance(mapper.compressor, ZlibCompressor)
        self.assertIsNone(mapper.cipher)

        # Create mapper with compressor module as topic.
        self.env[self.factory.COMPRESSOR_TOPIC] = "zlib"
        mapper = self.factory.mapper(transcoder=self.transcoder)
        self.assertIsInstance(mapper, Mapper)
        self.assertEqual(mapper.compressor, zlib)
        self.assertIsNone(mapper.cipher)

    def test_createmapper_with_cipher(self):

        # Check cipher needs a key.
        self.env[self.factory.CIPHER_TOPIC] = get_topic(AESCipher)

        with self.assertRaises(EnvironmentError):
            self.factory.mapper(transcoder=self.transcoder)

        # Check setting key but no topic defers to AES.
        del self.env[self.factory.CIPHER_TOPIC]

        cipher_key = AESCipher.create_key(16)
        self.env[self.factory.CIPHER_KEY] = cipher_key

        # Create mapper with cipher.
        mapper = self.factory.mapper(transcoder=self.transcoder)
        self.assertIsInstance(mapper, Mapper)
        self.assertIsNotNone(mapper.cipher)
        self.assertIsNone(mapper.compressor)

    def test_createmapper_with_cipher_and_compressor(
        self,
    ):

        # Create mapper with cipher and compressor.
        self.env[self.factory.COMPRESSOR_TOPIC] = get_topic(ZlibCompressor)

        self.env[self.factory.CIPHER_TOPIC] = get_topic(AESCipher)
        cipher_key = AESCipher.create_key(16)
        self.env[self.factory.CIPHER_KEY] = cipher_key

        mapper = self.factory.mapper(transcoder=self.transcoder)
        self.assertIsInstance(mapper, Mapper)
        self.assertIsNotNone(mapper.cipher)
        self.assertIsNotNone(mapper.compressor)

    def test_mapper_with_wrong_cipher_key(self):
        self.env.name = "App1"
        self.env[self.factory.CIPHER_TOPIC] = get_topic(AESCipher)
        cipher_key1 = AESCipher.create_key(16)
        cipher_key2 = AESCipher.create_key(16)
        self.env["APP1_" + self.factory.CIPHER_KEY] = cipher_key1
        self.env["APP2_" + self.factory.CIPHER_KEY] = cipher_key2

        mapper1: Mapper = self.factory.mapper(
            transcoder=self.transcoder,
        )

        domain_event = DomainEvent(
            originator_id=uuid4(),
            originator_version=1,
            timestamp=datetime.now(tz=TZINFO),
        )
        stored_event = mapper1.from_domain_event(domain_event)
        copy = mapper1.to_domain_event(stored_event)
        self.assertEqual(domain_event.originator_id, copy.originator_id)

        self.env.name = "App2"
        mapper2: Mapper = self.factory.mapper(
            transcoder=self.transcoder,
        )
        # This should fail because the infrastructure factory
        # should read different cipher keys from the environment.
        with self.assertRaises(ValueError):
            mapper2.to_domain_event(stored_event)

    def test_create_aggregate_recorder(self):
        recorder = self.factory.aggregate_recorder()
        self.assertEqual(type(recorder), self.expected_aggregate_recorder_class())

        self.assertIsInstance(recorder, AggregateRecorder)

        # Exercise code path where table is not created.
        self.env["CREATE_TABLE"] = "f"
        recorder = self.factory.aggregate_recorder()
        self.assertEqual(type(recorder), self.expected_aggregate_recorder_class())

    def test_create_application_recorder(self):
        recorder = self.factory.application_recorder()
        self.assertEqual(type(recorder), self.expected_application_recorder_class())
        self.assertIsInstance(recorder, ApplicationRecorder)

        # Exercise code path where table is not created.
        self.env["CREATE_TABLE"] = "f"
        recorder = self.factory.application_recorder()
        self.assertEqual(type(recorder), self.expected_application_recorder_class())

    def test_create_process_recorder(self):
        recorder = self.factory.process_recorder()
        self.assertEqual(type(recorder), self.expected_process_recorder_class())
        self.assertIsInstance(recorder, ProcessRecorder)

        # Exercise code path where table is not created.
        self.env["CREATE_TABLE"] = "f"
        recorder = self.factory.process_recorder()
        self.assertEqual(type(recorder), self.expected_process_recorder_class())
