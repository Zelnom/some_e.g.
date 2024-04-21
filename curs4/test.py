import unittest
import numbers

class PerfectSquareTests(unittest.TestCase):
    def test_imperfect_perfect_square(self):
        #datele problemei
        number = 10
        is_perfect_square = numbers.perfect_square(number)
        assert not is_perfect_square

    def test_perfect_square(self):
        number = 9
        is_perfect_square = numbers.perfect_square(number)
        assert is_perfect_square
        