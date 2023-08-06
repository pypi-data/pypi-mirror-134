# -*- coding: utf-8 -*-

import typing
from datetime import datetime


class Bucket:
    def __init__(self, data: dict):
        self.name: str = data.get("name")
        self.owner_identity: dict = data.get("ownerIdentity", dict())
        self.arn: str = data.get("arn")


class Object:
    def __init__(self, data: dict):
        self.key: str = data.get("key")
        self.sequencer: str = data.get("sequencer")


class S3:
    def __init__(self, data: dict):
        self.s3Schema_version: str = data.get("s3SchemaVersion")
        self.configuration_id: str = data.get("configurationId")
        self.bucket: Bucket = Bucket(data.get("bucket", dict()))
        self.object: Object = Object(data.get("object", dict()))


class S3DeleteRecord:
    def __init__(self, data: dict):
        self.event_version: str = data.get("eventVersion")
        self.event_source: str = data.get("eventSource")
        self.aws_region: str = data.get("awsRegion")
        self.event_time: str = data.get("eventTime")
        self.event_name: str = data.get("eventName")
        self.user_identity: dict = data.get("userIdentity", dict())
        self.request_parameters: dict = data.get("requestParameters", dict())
        self.response_elements: dict = data.get("responseElements", dict())
        self.s3: S3 = S3(data.get("s3", dict()))

    @property
    def event_datetime(self) -> datetime:
        return datetime.strptime(self.event_time, "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def bucket(self) -> str:
        return self.s3.bucket.name

    @property
    def key(self) -> str:
        return self.s3.object.key


class S3DeleteEvent:
    def __init__(self, data: dict):
        self.records: typing.List[S3DeleteRecord] = [
            S3DeleteRecord(dct)
            for dct in data.get("Records")
        ]
