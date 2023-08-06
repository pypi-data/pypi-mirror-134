# This file is placed in the Public Domain.


"OTP-CR-117/19"


import os
import unittest


from gcd.obj import Object, keys, values
from gcd.tbl import Tbl


import gcd.mod.bsc


Tbl.add(gcd.mod.bsc)


class Test_Table(unittest.TestCase):

    def test_mod(self):
        self.assertTrue("gcd.mod.bsc" in keys(Tbl.mod))
