import leapyear
import unittest
import pytest

#pytest
def test_is_leapyear():
    assert leapyear.is_leapyear(2020)

def test_is_leapyear2():
    assert leapyear.is_leapyear(1800)
    #should fail

def test_is_leapyear3():
    assert leapyear.is_leapyear(2100)
    #should fail

def test_is_leapyear4():
    assert leapyear.is_leapyear(2000)

#unittest
#python -m unittest test_leapyear.py
class test_class(unittest.TestCase):
    def test_is_leapyear5(self):
        self.assertTrue(leapyear.is_leapyear(2400))

    def test_is_leapyear6(self):
        self.assertFalse(leapyear.is_leapyear(2300))
