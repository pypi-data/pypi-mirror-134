# This file is placed in the Public Domain.


"debug"


class TestError(Exception):

    pass


def rse(event):
    raise TestError("bla")
