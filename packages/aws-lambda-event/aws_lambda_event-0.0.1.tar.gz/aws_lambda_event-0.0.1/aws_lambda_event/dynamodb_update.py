# -*- coding: utf-8 -*-

import typing
import attr
from attrs_mate import AttrsClass


@attr.s
class DynamodbDetails(AttrsClass):
    Keys: typing.Dict[str, typing.Dict[str, str]] = attr.ib(default=None)
    NewImage: typing.Dict[str, typing.Dict[str, str]] = attr.ib(default=None)
    OldImage: typing.Dict[str, typing.Dict[str, str]] = attr.ib(default=None)
    ApproximateCreationDateTime: int = attr.ib(default=None)
    SequenceNumber: dict = attr.ib(default=None)
    SizeBytes: int = attr.ib(default=None)
    StreamViewType: dict = attr.ib(default=None)


@attr.s
class DynamodbUpdateRecord(AttrsClass):
    eventID: str = attr.ib()
    eventName: str = attr.ib()
    eventVersion: str = attr.ib()
    eventSource: str = attr.ib()
    awsRegion: str = attr.ib()
    eventSourceARN: str = attr.ib()
    dynamodb: DynamodbDetails = DynamodbDetails.ib_nested()

    @property
    def keys(self) -> typing.Dict[str, typing.Dict[str, str]]:
        return self.dynamodb.Keys

    @property
    def new_image(self) -> typing.Dict[str, typing.Dict[str, str]]:
        return self.dynamodb.NewImage

    @property
    def old_image(self) -> typing.Dict[str, typing.Dict[str, str]]:
        return self.dynamodb.OldImage


@attr.s
class DynamodbUpdateEvent(AttrsClass):
    Records: typing.List[DynamodbUpdateRecord] = DynamodbUpdateRecord.ib_list_of_nested()

    @property
    def records(self) -> typing.List[DynamodbUpdateRecord]:
        return self.Records
