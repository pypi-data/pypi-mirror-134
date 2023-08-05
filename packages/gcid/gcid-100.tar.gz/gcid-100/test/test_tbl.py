# This file is placed in the Public Domain.


"OTP-CR-117/19"


import os
import unittest


from gcid.obj import Object, keys, values
from gcid.tbl import Tbl


import gcid.mod.bsc


Tbl.add(gcid.mod.bsc)


class Test_Table(unittest.TestCase):

    def test_mod(self):
        self.assertTrue("gcid.mod.bsc" in keys(Tbl.mod))
