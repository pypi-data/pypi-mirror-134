# This file is placed in the Public Domain.


"handler"


import queue
import time
import _thread


from .evt import Event
from .obj import Object
from .tbl import Cmd
from .thr import launch
from .utl import locked


cmdlock = _thread.allocate_lock()


class Stop(Exception):

    pass


class Handler(Object):

    def __init__(self):
        Object.__init__(self)
        self.errors = []
        self.queue = queue.Queue()
        self.stopped = False

    def event(self, txt, origin=None):
        e = Event()
        e.orig = repr(self)
        e.origin = origin or "user@handler"
        e.txt = txt
        return e

    @locked(cmdlock)
    def handle(self, e):
        Cmd.handle(e)

    def loop(self):
        while not self.stopped:
            try:
                e = self.poll()
                if e:
                    self.handle(e)
            except Stop:
                break

    def poll(self):
        return self.queue.get()

    def put(self, e):
        self.queue.put_nowait(e)

    def restart(self):
        self.stop()
        self.start()

    def start(self):
        launch(self.loop)

    def stop(self):
        self.stopped = True
        self.queue.put(None)

    def wait(self):
        while 1:
            time.sleep(1.0)
