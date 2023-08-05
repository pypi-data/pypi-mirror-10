#!/usr/bin/env python
# coding=utf-8
# Filename: jpp.py
# pylint: disable=
"""
Pump for the jpp file read through aanet interface.

"""
from __future__ import division, absolute_import, print_function

from km3pipe import Pump
from km3pipe.logger import logging

from controlhost import Client

log = logging.getLogger(__name__)  # pylint: disable=C0103


class CHPump(Pump):
    """A pump for ControlHost data."""

    def __init__(self, **context):
        super(self.__class__, self).__init__(**context)

        self.host = self.get('host')
        self.port = self.get('port') or 5553
        self.tag = self.get('tag') or 'foo'

        self.client = Client(host, port)
        self.client._connect()
        self.client.subscribe(tag)

    def process(self, blob):
        prefix, message = self.client.get_message()
        return {'CHPrefix': prefix, 'CHMessage': message}

    def finish(self):
        self.client._disconnect()
