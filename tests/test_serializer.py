# -*- coding: utf-8 -*-
import unittest

from ddby import Money, Currency, get_currency
from ddby.serializer import Serializer
from ddby.error import IncorrectSerializeFormat

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
            IncorrectSerializeFormat,
            serializer.unserialize,
            string
        )

    def test_unserialize_throws_if_amount_is_not_numeric(self):
        string = "1:banana:USD:2"

        serializer = Serializer()

        self.assertRaises(
            IncorrectSerializeFormat,
            serializer.unserialize,
            string
        )

    def test_serialize_with_zero_precision(self):
        m = Money(500, 'JPY')
        expected = '1:500:JPY:0'

        serializer = Serializer()
        actual = serializer.serialize(m)

        assert actual == expected

if __name__ == '__main__':
    unittest.main()

