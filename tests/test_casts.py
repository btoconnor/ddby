# -*- coding: utf-8 -*-
import unittest

from ddby import Money, Currency, get_currency
from ddby.exchange import static

class TestCasts(unittest.TestCase):

    def test_cast_to_float(self):
        m = Money(4050, 'USD')
        expected = 40.50

        actual = float(m)

        assert actual == expected, "{0} != {1}".format(actual, expected)

    def test_cast_to_float_hundreds(self):
        m = Money(4051, 'USD')
        expected = 40.51

        actual = float(m)

        assert actual == expected, "{0} != {1}".format(actual, expected)

    def test_cast_to_float_with_zero_precision(self):
        m = Money(4051, 'JPY')
        expected = 4051.0

        actual = float(m)

        assert actual == expected, "{0} != {1}".format(actual, expected)


if __name__ == '__main__':
    unittest.main()
