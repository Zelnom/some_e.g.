import unittest
import numbers

class NumbersTests(unittest.TestCase):
    def test_even_number(self):
        number = 6
        # when
        is_even = numbers.even_number(number)
        # then
        assert is_even

#asser it's like an if
    def test_uneven_number(self):
        number = 7
        is_even = numbers.even_number(number)
        assert not is_even