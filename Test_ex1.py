# -*- coding: utf-8 -*-
import unittest
from Ex1 import *


class Test_ex1(unittest.TestCase):
    def reverse_sentence(self):
        text = "ala ma kota"
        self.assertEquals(reverse_sentence(text), "kota ma ala")
        text = "żołte żąkile"
        self.assertEquals(reverse_sentence(text), "żąkile żołte")
        text = "a"
        self.assertEquals(reverse_sentence(text), "a")
        text = " "
        self.assertEquals(reverse_sentence(text), "")
        text = "this is Kate's balloon"
        self.assertEquals(reverse_sentence(text), "balloon Kate's is this")
