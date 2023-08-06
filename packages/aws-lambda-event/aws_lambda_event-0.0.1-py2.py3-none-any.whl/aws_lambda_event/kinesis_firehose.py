# -*- coding: utf-8 -*-

import typing
import base64

import attr
from datetime import datetime
from attrs_mate import AttrsClass


@attr.s
class KinesisFirehoseRecord(AttrsClass):
    recordId: str = attr.ib()
    approximateArrivalTimestamp: int = attr.ib()
    data: str = attr.ib()

    @property
    def binary_data(self) -> bytes:
        return base64.b64decode(self.data.encode("utf-8"))

    @property
    def approximate_arrival_time(self) -> datetime:
        return datetime.fromtimestamp(self.approximateArrivalTimestamp / 1000)


@attr.s
class KinesisFirehoseEvent(AttrsClass):
    invocationId: str = attr.ib()
    deliveryStreamArn: str = attr.ib()
    region: str = attr.ib()
    records: typing.List[KinesisFirehoseRecord] = KinesisFirehoseRecord.ib_list_of_nested()
