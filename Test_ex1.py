# -*- coding: utf-8 -*-
import unittest
from Ex1 import *


class Test_ex1(unittest.TestCase):
    def test_reversing(self):
        text = "ala ma kota"
        self.assertEquals(reversing(text), "kota ma ala")
        text = "żołte żąkile"
        self.assertEquals(reversing(text), "żąkile żołte")
        text = "a"
        self.assertEquals(reversing(text), "a")
        text = " "
        self.assertEquals(reversing(text), "")
        text = "this is Kate's balloon"
        self.assertEquals(reversing(text), "balloon Kate's is this")
