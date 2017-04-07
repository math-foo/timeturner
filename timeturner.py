#!/usr/bin/python3

import datetime

ORIG_DATETIME = datetime.datetime

class Freeze(object):
    def __init__(self, freeze_time):
        self.freeze_time = freeze_time

    def __enter__(self):
        datetime.datetime = _FreezeDatetime
        datetime.datetime.freeze_time = self.freeze_time

    def __exit__(self, *args):
        datetime.datetime = ORIG_DATETIME

class _FreezeDatetime(datetime.datetime):
    freeze_time = None

    @classmethod
    def today(cls):
        return cls.freeze_time

    @classmethod
    def now(cls):
        return cls.freeze_time

    @classmethod
    def utcnow(cls):
        return cls.freeze_time
