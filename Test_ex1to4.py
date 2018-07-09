# -*- coding: utf-8 -*-
import unittest
from Ex1to4 import *


class TestEx1to4(unittest.TestCase):

    def setUp(self):
        self.string1 = "she sells sea shells"
        self.string2 = "two tea to room two two"
        self.string3 = "three witches watch three Swatch watches. Which witch watch which Swatch watch"
        self.string4 = "ala ma kota"
        self.string5 = "żołte żąkile"
        self.string6 = "a"
        self.string7 = ' '
        self.string8 = "this is Kate's balloon"

    def test_reverse_sentence(self):
        self.assertEquals(reverse_sentence(self.string4), "kota ma ala")
        self.assertEquals(reverse_sentence(self.string5), "żąkile żołte")
        self.assertEquals(reverse_sentence(self.string6), "a")
        self.assertEquals(reverse_sentence(self.string7), "")
        self.assertEquals(reverse_sentence(self.string8), "balloon Kate's is this")

    def test_count_digits(self):
        digit1 = 12345555
        self.assertEquals(count_digits(digit1), 5)
        digit2 = 4460404787
        self.assertEquals(count_digits(digit2), 5)
        digit3 = 000
        self.assertEquals(count_digits(digit3), 1)
        digit4 = 98766789
        self.assertEquals(count_digits(digit4), 4)

    def test_isPalindrome(self):
        string4 = "Anna"
        self.assertEquals(isPalindrome(string4), True)
        string5 = "A toyota"
        self.assertEquals(isPalindrome(string5), True)
        string6 = "11 02 2011"
        self.assertEquals(isPalindrome(string6), True)
        self.assertEquals(isPalindrome(self.string1), False)
        self.assertEquals(isPalindrome(self.string2), False)
        self.assertEquals(isPalindrome(self.string3), False)
        self.assertEquals(isPalindrome(self.string4), False)
        self.assertEquals(isPalindrome(self.string6), True)

    def test_convert_to_phone_keyboard_style(self):
        string1 = "eve has a cat"
        self.assertEquals(convert_to_phone_keyboard_style(string1), "3388833#4427777#2#22228")
        pass


