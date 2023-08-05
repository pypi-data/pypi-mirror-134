# This file is placed in the Public Domain.


"OTP-CR-117/19"


import unittest


from gcid.krn import Cfg


class Test_Kernel(unittest.TestCase):

    def test_cfg(self):
        self.assertTrue("gcid.krn.Cfg" in str(Cfg))
