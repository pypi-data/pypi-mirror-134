# -*- coding: utf-8 -*-

import typing
import base64
from datetime import datetime
from .helpers import datetime_from_timestamp


class Kinesis:
    def __init__(self, data: dict):
        self.partition_key: str = data.get("partitionKey")
        self.kinesis_schema_version: str = data.get("kinesisSchemaVersion")
        self.data: str = data.get("data")
        self.sequence_number: str = data.get("sequenceNumber")
        self.approximate_arrival_timestamp: int = data.get("approximateArrivalTimestamp")

    @property
    def binary_data(self) -> bytes:
        return base64.b64decode(self.data.encode("utf-8"))

    @property
    def approximate_arrival_datetime(self) -> datetime:
        return datetime_from_timestamp(self.approximate_arrival_timestamp)


class KinesisStreamRecord:
    def __init__(self, data: dict):
        self.event_source: str = data.get("eventSource")
        self.event_id: str = data.get("eventID")
        self.invoke_identity_arn: str = data.get("invokeIdentityArn")
        self.event_version: str = data.get("eventVersion")
        self.event_name: str = data.get("eventName")
        self.event_source_arn: str = data.get("eventSourceARN")
        self.aws_region: str = data.get("awsRegion")
        self.kinesis: Kinesis = Kinesis(data.get("kinesis", dict()))

    @property
    def kinesis_partition_key(self) -> str:
        return self.kinesis.partition_key

    @property
    def kinesis_binary_data(self) -> bytes:
        return self.kinesis.binary_data

    @property
    def kinesis_sequence_number(self) -> str:
        return self.kinesis.sequence_number

    @property
    def kinesis_approximate_arrival_datetime(self) -> datetime:
        return self.kinesis.approximate_arrival_datetime


class KinesisStreamEvent:
    def __init__(self, data: dict):
        self.records: typing.List[KinesisStreamRecord] = [
            KinesisStreamRecord(dct)
            for dct in data.get("Records", [])
        ]
