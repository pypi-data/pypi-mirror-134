# -*- coding: utf-8 -*-

import typing
from datetime import datetime
from .helpers import datetime_from_timestamp


class Dynamodb:
    def __init__(self, data: dict):
        self.keys: typing.Dict[str, typing.Dict[str, str]] = data.get("Keys", dict())
        self.new_image: typing.Dict[str, typing.Dict[str, str]] = data.get("NewImage", dict())
        self.old_image: typing.Dict[str, typing.Dict[str, str]] = data.get("OldImage", dict())
        self.approximate_creation_timestamp: int = data.get("ApproximateCreationDateTime")
        self.sequence_number: dict = data.get("SequenceNumber")
        self.size_bytes: int = data.get("SizeBytes")
        self.stream_view_type: dict = data.get("StreamViewType")

    @property
    def approximate_creation_datetime(self) -> datetime:
        return datetime_from_timestamp(self.approximate_creation_timestamp)


class DynamodbUpdateRecord:
    def __init__(self, data: dict):
        self.event_id: str = data.get("eventID")
        self.event_name: str = data.get("eventName")
        self.event_version: str = data.get("eventVersion")
        self.event_source: str = data.get("eventSource")
        self.aws_region: str = data.get("awsRegion")
        self.event_source_arn: str = data.get("eventSourceARN")
        self.dynamodb: Dynamodb = Dynamodb(data.get("dynamodb"))

    @property
    def keys(self) -> typing.Dict[str, typing.Dict[str, str]]:
        return self.dynamodb.keys

    @property
    def new_image(self) -> typing.Dict[str, typing.Dict[str, str]]:
        return self.dynamodb.new_image

    @property
    def old_image(self) -> typing.Dict[str, typing.Dict[str, str]]:
        return self.dynamodb.old_image

    @property
    def approximate_creation_timestamp(self) -> int:
        return self.dynamodb.approximate_creation_timestamp

    @property
    def approximate_creation_datetime(self) -> datetime:
        return self.dynamodb.approximate_creation_datetime


class DynamodbUpdateEvent:
    def __init__(self, data: dict):
        self.records: typing.List[DynamodbUpdateRecord] = [
            DynamodbUpdateRecord(dct)
            for dct in data.get("Records")
        ]
