# -*- coding: utf-8 -*-

"""
Class Interface for AWS Lambda event.
"""

from ._version import __version__

__short_description__ = "Class Interface for AWS Lambda event."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from .s3_put import S3PutEvent
    from .s3_delete import S3DeleteEvent
    from .sns import SNSTopicNotificationEvent
    from .sqs import SQSEvent
    from .dynamodb_update import DynamodbUpdateEvent
    from .kinesis_stream import KinesisStreamEvent
    from .kinesis_firehose import KinesisFirehoseEvent
except ImportError:  # pragma: no cover
    pass
except:  # pragma: no cover
    raise
