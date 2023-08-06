# This file is placed in the Public Domain.


"OTP-CR-117/19"


import unittest


from gcd.dbs import Db
from gcd.obj import Object
from gcd.jsn import dumps, loads


class Composite(Object):

    def __init__(self):
        super().__init__()
        self.db = Db()



class Test_Composite(unittest.TestCase):

    def test_composite(self):
        c = Composite()
        s = dumps(c)
        a = loads(dumps(c))
        self.assertEqual(type(a.db), type({}))
