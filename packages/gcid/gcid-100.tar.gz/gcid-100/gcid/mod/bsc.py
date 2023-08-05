# This file is placed in the Public Domain.


"basic"


import threading
import time


from gcid.bus import Bus
from gcid.dbs import Db, fntime, save
from gcid.dbs import find
from gcid.fnc import format
from gcid.obj import Object, get, update
from gcid.tbl import Cmd
from gcid.thr import getname
from gcid.prs import elapsed


def __dir__():
    return (
        "cmd",
        "flt",
        "fnd",
        "log",
        "thr",
        "upt"
    )

starttime = time.time()


class Log(Object):

    def __init__(self):
        super().__init__()
        self.txt = ""


def cmd(event):
    event.reply(",".join(sorted(Cmd.cmds)))


def flt(event):
    try:
        index = int(event.args[0])
        event.reply(Bus.objs[index])
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(" | ".join([getname(o) for o in Bus.objs]))


def fnd(event):
    if not event.args:
        db = Db()
        event.reply(",".join(
            sorted({x.split(".")[-1].lower() for x in db.types()}))
        )
        return
    otype = event.args[0]
    nr = -1
    got = False
    for fn, o in find(otype):
        nr += 1
        txt = "%s %s" % (str(nr), format(o))
        if "t" in event.opts:
            txt = txt + " %s" % (elapsed(time.time() - fntime(fn)))
        got = True
        event.reply(txt)
    if not got:
        event.reply("no result")

def log(event):
    if not event.rest:
        event.reply("log <txt>")
        return
    o = Log()
    o.txt = event.rest
    save(o)
    event.reply("ok")


def thr(event):
    result = []
    for t in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(t).startswith("<_"):
            continue
        o = Object()
        update(o, vars(t))
        if get(o, "sleep", None):
            up = o.sleep - int(time.time() - o.state.latest)
        else:
            up = int(time.time() - starttime)
        thrname = t.getName()
        if not thrname:
            continue
        if thrname:
            result.append((up, thrname))
    res = []
    for up, txt in sorted(result, key=lambda x: x[0]):
        res.append("%s(%s)" % (txt, elapsed(up)))
    if res:
        event.reply(" ".join(res))


def upt(event):
    event.reply(elapsed(time.time() - starttime))
