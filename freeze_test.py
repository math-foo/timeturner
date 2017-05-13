#!/usr/bin/python3

import datetime
import timeturner
import unittest


class FreezeTest(unittest.TestCase):

    def test_frozen_datetime_today(self):
        past_datetime = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_datetime):
            today = datetime.datetime.today()
            self.assertEqual(today, past_datetime)

        today = datetime.datetime.today()
        self.assertNotEqual(today, past_datetime)

    def test_frozen_datetime_now(self):
        past_datetime = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_datetime):
            now = datetime.datetime.now()
            self.assertEqual(now, past_datetime)

        now = datetime.datetime.now()
        self.assertNotEqual(now, past_datetime)

    def test_frozen_datetime_utcnow(self):
        past_datetime = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_datetime):
            utcnow = datetime.datetime.now()
            self.assertEqual(utcnow, past_datetime)

        utcnow = datetime.datetime.utcnow()
        self.assertNotEqual(utcnow, past_datetime)

    def test_frozen_datetime_isinstance(self):
        past_datetime = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_datetime):
            now = datetime.datetime.now()
            self.assertTrue(isinstance(now, datetime.datetime))

        now = datetime.datetime.now()
        self.assertTrue(isinstance(now, datetime.datetime))

    def test_frozen_datetime_other_datetime(self):
        past_datetime = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_datetime):
            now = datetime.datetime.now()
            also_now = datetime.datetime(1990, 1, 1, 10, 0)
            self.assertEqual(now, also_now)

        also_past = datetime.datetime(1990, 1, 1, 10, 0)
        self.assertEqual(past_datetime, also_past)

