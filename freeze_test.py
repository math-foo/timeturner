#!/usr/bin/python3

import datetime
import timeturner
import unittest


class FreezeTest(unittest.TestCase):

    def test_freeze_today(self):
        past_time = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_time):
            today = datetime.datetime.today()
            self.assertEquals(today, past_time)

        today = datetime.datetime.today()
        self.assertNotEqual(today, past_time)

    def test_freeze_now(self):
        past_time = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_time):
            now = datetime.datetime.now()
            self.assertEquals(now, past_time)

        now = datetime.datetime.now()
        self.assertNotEqual(now, past_time)

    def test_freeze_utcnow(self):
        past_time = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_time):
            utcnow = datetime.datetime.utcnow()
            self.assertEquals(utcnow, past_time)

        utcnow = datetime.datetime.utcnow()
        self.assertNotEqual(utcnow, past_time)
          
