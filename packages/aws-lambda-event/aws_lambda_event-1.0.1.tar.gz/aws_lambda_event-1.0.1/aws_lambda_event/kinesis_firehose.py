# -*- coding: utf-8 -*-

import typing
import base64
from datetime import datetime
from .helpers import datetime_from_timestamp


class KinesisFirehoseRecord:
    def __init__(self, data: dict):
        self.record_id: str = data.get("recordId")
        self.approximate_arrival_timestamp: int = data.get("approximateArrivalTimestamp")
        self.data: str = data.get("data")

    @property
    def binary_data(self) -> bytes:
        return base64.b64decode(self.data.encode("utf-8"))

    @property
    def approximate_arrival_datetime(self) -> datetime:
        return datetime_from_timestamp(self.approximate_arrival_timestamp)


class KinesisFirehoseEvent:
    def __init__(self, data: dict):
        self.invocationId: str = data.get("invocationId")
        self.deliveryStreamArn: str = data.get("deliveryStreamArn")
        self.region: str = data.get("region")
        self.records: typing.List[KinesisFirehoseRecord] = [
            KinesisFirehoseRecord(dct)
            for dct in data.get("records", [])
        ]
