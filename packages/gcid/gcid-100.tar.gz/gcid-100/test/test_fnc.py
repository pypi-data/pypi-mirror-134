# This file is placed in the Public Domain.


import os
import unittest

from gcid.obj import *
from gcid.cfg import *
from gcid.dbs import *
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

    def test_cdir(self):
        cdir(".test")
        self.assertTrue(os.path.exists(".test"))

    def test_edit(self):
        o = Object()
        d = {"key": "value"}
        edit(o, d)
        self.assertEqual(o.key, "value")

    def test_format(self):
        o = Object()
        self.assertEqual(format(o), "")

    def test_fns(self):
        Cfg.wd = ".test"
        o = Object()
        save(o)
        self.assertTrue("Object" in fns("gcid.obj.Object")[0])

    def test_hook(self):
        o = Object()
        o.key = "value"
        p = save(o)
        oo = hook(p)
        self.assertEqual(oo.key, "value")

    def test_last(self):
        o = Object()
        o.key = "value"
        save(o)
        last(o)
        self.assertEqual(o.key, "value")

    def test_load(self):
        o = Object()
        o.key = "value"
        p = save(o)
        oo = Object()
        load(oo, p)
        self.assertEqual(oo.key, "value")

    def test_register(self):
        o = Object()
        register(o, "key", "value")
        self.assertEqual(o.key, "value")

    def test_save(self):
        Cfg.wd = ".test"
        o = Object()
        p = save(o)
        self.assertTrue(os.path.exists(os.path.join(Cfg.wd, "store", p)))
