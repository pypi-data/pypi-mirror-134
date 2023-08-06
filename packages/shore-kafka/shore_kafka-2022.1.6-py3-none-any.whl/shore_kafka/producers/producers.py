import logging
from typing import Any, Callable, List, Union
from uuid import uuid1

import pydantic
from confluent_kafka.cimpl import Producer as _ProducerImpl
from confluent_kafka.error import KeySerializationError, ValueSerializationError
from confluent_kafka.serialization import MessageField, SerializationContext, StringSerializer

from ..schema_registry import SchemaRegistryClient, ShoreSerializer

logger = logging.getLogger(__file__)


class ShoreProducer(_ProducerImpl):
    def __init__(
        self,
        kafka_conf: dict,
        sr_conf: dict,
        client_id=None,
        **extra_confs,
    ):

        # set properties
        self.kafka_conf = kafka_conf
        self.sr_conf = sr_conf
        self.client_id = client_id if client_id is not None else uuid1().hex[8:]

        # for debug
        self.sr_client = SchemaRegistryClient(self.sr_conf)
        self.conf = {**kafka_conf, "client.id": self.client_id, **extra_confs}

        # set serializer
        self.serializer = dict()

        super(ShoreProducer, self).__init__(self.conf)

    def produce(
        self,
        topic: str,
        key: Union[str, pydantic.BaseModel] = None,
        value: Union[str, pydantic.BaseModel] = None,
        partition: int = -1,
        on_delivery: Callable = None,
        timestamp: int = 0,
        headers: List[tuple] = None,
    ) -> Any:
        """produce

        :param topic: topic name
        :type topic: str
        :param key: message key, defaults to None
        :type key: Union[str, pydantic.BaseModel], optional
        :param value: message value, defaults to None
        :type value: Union[str, pydantic.BaseModel], optional
        :param partition: patrition, defaults to -1
        :type partition: int, optional
        :param on_delivery: callback on delivery, defaults to None
        :type on_delivery: Callable, optional
        :param timestamp: kafka timstamp in milli-seconds, defaults to 0
        :type timestamp: int, optional
        :param headers: message headers [(key, value), ...], defaults to None
        :type headers: List[tuple], optional
        :raises KeySerializationError:
        :raises ValueSerializationError:
        :return: return of on_delivery callback
        :rtype: Any
        """
        if topic not in self.serializer.keys():
            self.serializer[topic] = {
                "key": ShoreSerializer(self.sr_client, topic=topic, field="key"),
                "value": ShoreSerializer(self.sr_client, topic=topic, field="value"),
            }

        # serializer key
        if self.serializer[topic]["key"] is not None:
            try:
                key = self.serializer[topic]["key"](key)
            except Exception as se:
                raise KeySerializationError(se)

        # serializer value
        if self.serializer[topic]["value"] is not None:
            try:
                value = self.serializer[topic]["value"](value)
            except Exception as se:
                raise ValueSerializationError(se)

        # use default if delivery report is not given
        on_delivery = on_delivery if on_delivery is not None else self._default_delivery_report

        # produce
        super(ShoreProducer, self).produce(
            topic, value, key, headers=headers, partition=partition, timestamp=timestamp, on_delivery=on_delivery
        )

    @staticmethod
    def _ensure_list(x):
        if x is None or isinstance(x, list):
            return x
        return [x]

    @staticmethod
    def _default_delivery_report(err, msg):
        if err is not None:
            logger.error(f"FAILED | topic {msg.topic()} | error {err}")
        logger.info(f"SUCCEED | topic {msg.topic()} | partition {msg.partition()} | offset {msg.offset()}")
