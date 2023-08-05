# This file is placed in the Public Domain.


"OTP-CR-117/19"


import sys
import unittest


from gcid.bus import Bus
from gcid.clt import Client
from gcid.evt import Event
from gcid.fnc import format
from gcid.hdl import Handler
from gcid.krn import Cfg
from gcid.obj import Object, get, values
from gcid.tbl import Cls, Cmd, Tbl
from gcid.thr import launch


def getmain(name):
    return getattr(sys.modules["__main__"], name, None)


events = []


param = Object()
param.add = ["test@shell", "bart", ""]
param.cfg = ["nick=botje", "server=localhost", ""]
param.dlt = ["root@shell"]
param.dne = ["test4", ""]
param.dpl = ["reddit title,summary,link"]
param.flt = ["0", ""]
param.fnd = ["cfg", "log", "rss", "cfg server==localhost", "rss rss==reddit"]
param.log = ["test1", ""]
param.met = ["root@shell"]
param.nck = ["botje"]
param.pwd = ["bart blabla"]
param.rem = ["reddit", ""]
param.rss = ["https://www.reddit.com/r/python/.rss"]
param.tdo = ["things todo"]


class CLI(Client, Handler):

     def __init__(self):
         Client.__init__(self)
         Handler.__init__(self)

     def handle(self, e):
         launch(Handler.handle, self, e)
         e.wait()

     def raw(self, txt):
         print(txt)


     def raw(self, txt):
         results.append(txt)
        

c = CLI()
results = getmain("results")


class Test_Commands(unittest.TestCase):

    def setUp(self):
        c.start()
        
    def tearDown(self):
        c.stop()

    def test_commands(self):
        cmds = sorted(Cmd.cmds)
        for cmd in cmds:
            for ex in getattr(param, cmd, [""]):
                e = Event()
                e.txt = cmd + " " + ex
                e.orig = repr(c)
                c.put(e)
                events.append(e)
        consume(events)
        self.assertTrue(not events)


def consume(events):
    fixed = []
    res = []
    for e in events:
        e.wait()
        fixed.append(e)
    for f in fixed:
        try:
            events.remove(f)
        except ValueError:
            continue
    return res
