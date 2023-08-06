# -*- coding: utf-8 -*-

import typing
import attr
from attrs_mate import AttrsClass


@attr.s
class SNS(AttrsClass):
    Type: str = attr.ib()
    MessageId: str = attr.ib()
    TopicArn: str = attr.ib()
    Subject: str = attr.ib()
    Message: str = attr.ib()
    Timestamp: str = attr.ib()
    SignatureVersion: str = attr.ib()
    Signature: str = attr.ib()
    SigningCertUrl: str = attr.ib()
    UnsubscribeUrl: str = attr.ib()
    MessageAttributes: dict = attr.ib()


@attr.s
class SNSRecord(AttrsClass):
    EventSource: str = attr.ib()
    EventVersion: str = attr.ib()
    EventSubscriptionArn: str = attr.ib()
    Sns: SNS = SNS.ib_nested()

    @property
    def message(self) -> str:
        return self.Sns.Message

    @property
    def subject(self) -> str:
        return self.Sns.Subject

    @property
    def timestamp(self) -> str:
        return self.Sns.Timestamp


@attr.s
class SNSTopicNotificationEvent(AttrsClass):
    Records: typing.List[SNSRecord] = SNSRecord.ib_list_of_nested()

    @property
    def records(self) -> typing.List[SNSRecord]:
        return self.Records
