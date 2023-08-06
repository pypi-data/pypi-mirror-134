import json
import logging
import sys
import time
from abc import ABCMeta, abstractmethod

import boto3
import boto3.session

sqs_logger = logging.getLogger("sqs_listener")


################################################################
# SqsListener
# (TODO)
#  - error log 개선
################################################################
class SqsListener(object):
    """
    aws_conf = {
            "aws_access_key_id": <ACCESS_KEY_ID>,
            "aws_secret_access_key": <SECRET_ACCESS_KEY>,
            "region_name": <REGION_NAME>,
        }
    available kwargs
        - interval, default 60
        - visibility_timeout, default 600
        - message_attribute_names, default []
        - attribute_names, default []
        - force_delete, default False
        - wait_time, default 1
        - max_number_of_messages, default 1
    """

    __metaclass__ = ABCMeta

    def __init__(
        self,
        aws_conf: dict,
        queue_name: str,
        poll_interval: int = 60,
        wait_time: int = 1,
        max_number_of_messages: int = 1,
        force_delete: bool = False,
        **kwargs,
    ):

        # set properties
        self.aws_conf = aws_conf
        self.queue_name = queue_name
        self.poll_interval = poll_interval
        self.wait_time = wait_time
        self.max_number_of_messages = max_number_of_messages
        self.force_delete = force_delete

        # listener options
        self._queue_visibility_timeout = kwargs.get("visibility_timeout", "600")
        self._message_attribute_names = kwargs.get("message_attribute_names", [])
        self._attribute_names = kwargs.get("attribute_names", [])
        self._endpoint_name = kwargs.get("endpoint_name", None)

        # create client & get queue url
        self._session = boto3.session.Session()
        self._sqs_client = self._session.client("sqs", **aws_conf)
        self._queue_url = self._sqs_client.get_queue_url(QueueName=self.queue_name)["QueueUrl"]

    def once(self):
        messages = self._sqs_client.receive_message(
            QueueUrl=self._queue_url,
            MessageAttributeNames=self._message_attribute_names,
            AttributeNames=self._attribute_names,
            WaitTimeSeconds=self.wait_time,
            MaxNumberOfMessages=self.max_number_of_messages,
        )
        if "Messages" in messages:
            sqs_logger.debug(messages)
            sqs_logger.info(f"{len(messages['Messages'])} messages received")
            for m in messages["Messages"]:
                receipt_handle = m["ReceiptHandle"]
                m_body = m.get("Body", {})
                message_attribs = None
                attribs = None

                # catch problems with malformed JSON, usually a result of someone writing poor JSON directly in the AWS console
                try:
                    params_dict = json.loads(m_body)
                except Exception as ex:
                    sqs_logger.warning(f"Unable to parse message - JSON is not formatted properly, {ex}")
                    continue

                # attributes name is MessageAttributes or Attributes
                if "MessageAttributes" in m:
                    message_attribs = m["MessageAttributes"]
                if "Attributes" in m:
                    attribs = m["Attributes"]

                # Handle message and delete
                try:
                    if not self.force_delete:
                        result = self.handle_message(params_dict, message_attribs, attribs)
                        if result:
                            self._sqs_client.delete_message(QueueUrl=self._queue_url, ReceiptHandle=receipt_handle)
                    else:
                        self._sqs_client.delete_message(QueueUrl=self._queue_url, ReceiptHandle=receipt_handle)
                        self.handle_message(params_dict, message_attribs, attribs)
                except Exception as ex:
                    # need exception logtype to log stack trace
                    # (TODO) error log를 kafka topic에 남기는 것 해보기
                    sqs_logger.exception(ex)
        else:
            time.sleep(self.poll_interval)

    def listen(self):
        sqs_logger.info("Listening to queue " + self.queue_name)

        while True:
            # calling with WaitTimeSecconds of zero show the same behavior as not specifiying a wait time, ie: short polling
            self.once()

    def _prepare_logger(self):
        logger = logging.getLogger("eg_daemon")
        logger.setLevel(logging.INFO)

        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.INFO)

        formatstr = "[%(asctime)s - %(name)s - %(levelname)s]  %(message)s"
        formatter = logging.Formatter(formatstr)

        sh.setFormatter(formatter)
        logger.addHandler(sh)

    @abstractmethod
    def handle_message(self, body, attributes, messages_attributes) -> bool:
        """
        Implement this method to do something with the SQS message contents
        :param body: dict
        :param attributes: dict
        :param messages_attributes: dict
        :return:
        """
        return
