 import leapyear
 import unittest
 import pytest

 #pytest
 def test_is_leapyear():
     assert leapyear.is_leapyear(2020) == "true"

def test_is_leapyear2():
    assert leapyear.is_leapyear(1800) == "false"

def test_is_leapyear():
    assert leapyear.is_leapyear(2100) == "false"

def test_is_leapyear3():
    assert leapyear.is_leapyear(2000) == "true"

#unittest
class test_class(unittest.TestCase):
    def test_is_leapyear4(self):
        self.assertTrue(leapyear.is_leapyear(2400))

    def test_is_leapyear5(self):
        self.assertFalse(leapyear.is_leapyear(2300))
