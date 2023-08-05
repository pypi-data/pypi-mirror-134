# This file is placed in the Public Domain.


"OTP-CR-117/19"


import os
import unittest


from gcid.obj import *
from gcid.fnc import *



attr = (
    'clear',
    'copy',
    'fromkeys',
    'get',
    'items',
    'keys',
    'pop',
    'popitem',
    'setdefault',
    'update',
    'values'
)


class Test_ObjectFunctions(unittest.TestCase):


    def test_get(self):
        o = Object()
        o.key = "value"
        self.assertEqual(get(o, "key"), "value")

    def test_keys(self):
        o = Object()
        o.key = "value"
        self.assertEqual(
            list(keys(o)),
            [
                "key",
            ],
        )

    def test_items(self):
        o = Object()
        o.key = "value"
        self.assertEqual(
            list(items(o)),
            [
                ("key", "value"),
            ],
        )

    def test_update(self):
        o = Object()
        o.key = "value"
        oo = Object()
        update(oo, o)
        self.assertTrue(oo.key, "value")
        pass

    def test_values(self):
        o = Object()
        o.key = "value"
        self.assertEqual(
            list(values(o)),
            [
                "value",
            ],
        )
