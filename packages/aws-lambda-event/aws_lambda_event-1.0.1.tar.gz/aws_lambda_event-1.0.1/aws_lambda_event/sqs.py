# -*- coding: utf-8 -*-

import typing


class SQSRecord:
    def __init__(self, data: dict):
        self.message_id: str = data.get("messageId")
        self.receipt_handle: str = data.get("receiptHandle")
        self.body: str = data.get("body")
        self.attributes: dict = data.get("attributes")
        self.message_attributes: dict = data.get("messageAttributes")
        self.md5_of_body: str = data.get("md5OfBody")
        self.event_source: str = data.get("eventSource")
        self.event_source_arn: str = data.get("eventSourceARN")
        self.aws_region: str = data.get("awsRegion")


class SQSEvent:
    def __init__(self, data: dict):
        self.records: typing.List[SQSRecord] = [
            SQSRecord(dct)
            for dct in data.get("Records")
        ]
