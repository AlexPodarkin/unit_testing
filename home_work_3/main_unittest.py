import unittest
from home_work_3.main import Tasks


class Test(unittest.TestCase):
    def test_even_odd_number_test(self):
        self.assertTrue(Tasks.even_odd_number(10))
        self.assertFalse(Tasks.even_odd_number(11))

    def test_interval(self):
        self.assertTrue(Tasks.number_in_interval(30))
        self.assertFalse(Tasks.number_in_interval(10))
