# This file is placed in the Public Domain.


"OTP-CR-117/19"


import unittest


from gcd.fnc import edit
from gcd.krn import Cfg
from gcd.obj import Object, update
from gcd.prs import parse


class Test_Cfg(unittest.TestCase):

    def test_parse(self):
        p = Cfg()
        parse(p, "mod=irc")
        self.assertEqual(p.sets.mod, "irc")

    def test_parse2(self):
        p = Cfg()
        parse(p, "mod=irc,rss")
        self.assertEqual(p.sets.mod, "irc,rss")

    def test_edit(self):
        d = Object()
        update(d, {"mod": "irc,rss"})
        edit(Cfg, d)
        self.assertEqual(Cfg.mod, "irc,rss")
