# -*- coding: utf-8 -*-

import typing
from datetime import datetime


class SNS:
    def __init__(self, data: dict):
        self.type: str = data.get("Type")
        self.message_id: str = data.get("MessageId")
        self.topic_arn: str = data.get("TopicArn")
        self.subject: str = data.get("Subject")
        self.message: str = data.get("Message")
        self.timestamp: str = data.get("Timestamp")
        self.signature_version: str = data.get("SignatureVersion")
        self.signature: str = data.get("Signature")
        self.signing_cert_url: str = data.get("SigningCertUrl")
        self.unsubscribe_url: str = data.get("UnsubscribeUrl")
        self.message_attributes: dict = data.get("MessageAttributes")

    @property
    def datetime(self) -> datetime:
        return datetime.strptime(self.timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")


class SNSRecord:
    def __init__(self, data: dict):
        self.event_source: str = data.get("EventSource")
        self.event_version: str = data.get("EventVersion")
        self.event_subscription_arn: str = data.get("EventSubscriptionArn")
        self.sns: SNS = SNS(data.get("Sns", dict()))

    @property
    def message(self) -> str:
        return self.sns.message

    @property
    def subject(self) -> str:
        return self.sns.subject

    @property
    def datetime(self) -> datetime:
        return self.sns.datetime


class SNSTopicNotificationEvent:
    def __init__(self, data: dict):
        self.records: typing.List[SNSRecord] = [
            SNSRecord(dct)
            for dct in data.get("Records")
        ]
