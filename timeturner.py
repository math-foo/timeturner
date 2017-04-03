#!/usr/bin/python3

import datetime

real_datetime = datetime.datetime

class Freeze(object):
    def __init__(self, freeze_time):
        self.freeze_time = freeze_time

    def __enter__(self):
        datetime.datetime = _FreezeDatetime
        datetime.datetime.freeze_time = self.freeze_time

    def __exit__(self, *args):
        datetime.datetime = real_datetime

class _FreezeDatetime(datetime.datetime):
    freeze_time = None

    @classmethod
    def now(cls):
        return cls.freeze_time
