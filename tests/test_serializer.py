# -*- coding: utf-8 -*-
import unittest

from ddby import Money, Currency, get_currency
from ddby.serializer import Serializer

class TestExchange(unittest.TestCase):

    def test_serialize_with_precision(self):
        m = Money(500, 'USD')
        expected = "1:500:USD:2"

        serializer = Serializer()

        actual = serializer.serialize(m)

        assert expected == actual

    def test_unserialize_with_precision(self):
        string = "1:500:USD:2"
        expected = Money(500, 'USD')
        serializer = Serializer()

        actual = serializer.unserialize(string)

        assert expected == actual

    def test_unserialize_throws_error_if_incorrect_parts(self):
        string = "banana"
        
        serializer = Serializer()

        self.assertRaises(
            ValueError,
            serializer.unserialize,
            string
        )

    def test_unserialize_throws_if_amount_is_not_numeric(self):
        string = "1:banana:USD:2"

        serializer = Serializer()

        self.assertRaises(
            ValueError,
            serializer.unserialize,
            string
        )

    def test_serialize_with_zero_precision(self):
        m = Money(500, 'JPY')
        expected = '1:500:JPY:0'

        serializer = Serializer()
        actual = serializer.serialize(m)

        assert actual == expected

    def test_serialize_with_fractional_precision(self):
        m = Money(40003, 'USD', precision=3)
        expected = '1:40003:USD:3' # 40.003 USD

        serializer = Serializer()
        actual = serializer.serialize(m)

        assert actual == expected, "{0} != {1}".format(actual, expected)

    def test_unserialize_with_fractional_precision(self):
        string = "1:50003:USD:4"
        expected = Money(50003, 'USD', precision=4)
        serializer = Serializer()

        actual = serializer.unserialize(string)

        assert expected == actual


if __name__ == '__main__':
    unittest.main()

