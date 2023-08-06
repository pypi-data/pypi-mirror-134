# -*- coding: utf-8 -*-

import typing
import attr
from attrs_mate import AttrsClass


@attr.s
class SQSRecord(AttrsClass):
    messageId: str = attr.ib()
    receiptHandle: str = attr.ib()
    body: str = attr.ib()
    attributes: dict = attr.ib()
    messageAttributes: dict = attr.ib()
    md5OfBody: str = attr.ib()
    eventSource: str = attr.ib()
    eventSourceARN: str = attr.ib()
    awsRegion: str = attr.ib()


@attr.s
class SQSEvent(AttrsClass):
    Records: typing.List[SQSRecord] = SQSRecord.ib_list_of_nested()

    @property
    def records(self) -> typing.List[SQSRecord]:
        return self.Records
