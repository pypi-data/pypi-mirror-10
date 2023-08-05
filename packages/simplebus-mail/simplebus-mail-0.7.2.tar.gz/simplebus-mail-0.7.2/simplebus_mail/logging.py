# Copyright 2015 Vinicius Chiele. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Implements the logging related objects."""

from logging import Handler
from simplebus import current_bus
from simplebus_mail.mail import Mail
from simplebus_mail.mail import Message


class MailHandler(Handler):
    """Provides a logging handler to send email."""

    def __init__(self, sender, recipients, endpoint=None):
        super().__init__()

        if not isinstance(sender, str):
            raise TypeError('Parameter sender must be a string.')

        if not isinstance(recipients, list):
            raise TypeError('Parameter recipients must be a list.')

        if len(recipients) == 0:
            raise ValueError('Parameter recipients must have at least one address.')

        self.__mail = Mail()
        self.__mail.config.MAIL_DEFAULT_SENDER = sender
        self.__mail.config.MAIL_DEFAULT_RECIPIENTS = recipients
        self.__mail.config.MAIL_DEFAULT_ENDPOINT = endpoint

    def emit(self, record):
        """Creates a message from the record and sends through the bus."""

        self.__ensure_initialized()

        subject = self.__build_subject(record)
        body = self.format(record)
        message = Message(subject=subject, body=body)
        self.__mail.send(message)

    def __build_subject(self, record):
        """Builds a subject from the record."""

        subject = self.__mail.bus.app_id

        if subject:
            subject += ': '

        if record.msg:
            i = record.msg.find('\n')
            if i == -1:
                i = len(record.msg)
            subject += record.msg[:200] if i > 200 else record.msg[:i]

        return subject

    def __ensure_initialized(self):
        """Ensures the Mail instance is initialized."""

        if not self.__mail.bus:
            if not current_bus:
                raise RuntimeError('No Bus is running.')
            self.__mail.init_bus(current_bus)
