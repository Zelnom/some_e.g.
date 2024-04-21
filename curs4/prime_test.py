import unittest
import prime


class PrimeNumberTest(unittest.TestCase):
    def test_not_prime(self):
        # number = 23
        assert not prime.prime_num(22)

    def test_prime(self):
        # number = 23
        assert prime.prime_num(23)
