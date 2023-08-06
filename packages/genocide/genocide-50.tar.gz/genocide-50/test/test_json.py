# This file is placed in the Public Domain.


"OTP-CR-117/19"


import unittest


from gcd.jsn import dumps, loads
from gcd.obj import Object


validjson = '{"test": "bla"}'


class Test_JSON(unittest.TestCase):

    def test_json(self):
        o = Object()
        o.test = "bla"
        a = loads(dumps(o))
        self.assertEqual(a.test, "bla")

    def test_jsondump(self):
        o = Object()
        o.test = "bla"
        self.assertEqual(dumps(o), validjson)
