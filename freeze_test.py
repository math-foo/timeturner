#!/usr/bin/python3

import datetime
import timeturner
import unittest


class FreezeTest(unittest.TestCase):

    def test_freeze_past(self):
        past_time = datetime.datetime(1990, 1, 1, 10, 0)
        with timeturner.Freeze(past_time):
            current_time = datetime.datetime.now()
            self.assertEquals(current_time, past_time)

        current_time = datetime.datetime.now()
        self.assertNotEqual(current_time, past_time)
          
