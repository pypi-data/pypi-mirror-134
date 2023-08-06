# -*- coding: utf-8 -*-

import typing
import attr
from attrs_mate import AttrsClass


@attr.s
class Bucket(AttrsClass):
    name: str = attr.ib()
    ownerIdentity: dict = attr.ib()
    arn: str = attr.ib()


@attr.s
class Object(AttrsClass):
    key: str = attr.ib()
    size: int = attr.ib()
    eTag: str = attr.ib()
    sequencer: str = attr.ib()


@attr.s
class S3(AttrsClass):
    s3SchemaVersion: str = attr.ib()
    configurationId: str = attr.ib()
    bucket: Bucket = Bucket.ib_nested()
    object: Object = Object.ib_nested()


@attr.s
class S3PutRecord(AttrsClass):
    eventVersion: str = attr.ib()
    eventSource: str = attr.ib()
    awsRegion: str = attr.ib()
    eventTime: str = attr.ib()
    eventName: str = attr.ib()
    userIdentity: dict = attr.ib()
    requestParameters: dict = attr.ib()
    responseElements: dict = attr.ib()
    s3: S3 = S3.ib_nested()

    @property
    def bucket(self) -> str:
        return self.s3.bucket.name

    @property
    def key(self) -> str:
        return self.s3.object.key

    @property
    def etag(self) -> str:
        return self.s3.object.eTag

    @property
    def size(self) -> int:
        return self.s3.object.size


@attr.s
class S3PutEvent(AttrsClass):
    Records: typing.List[S3PutRecord] = S3PutRecord.ib_list_of_nested()

    @property
    def records(self) -> typing.List[S3PutRecord]:
        return self.Records
