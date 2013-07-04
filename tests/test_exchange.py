# -*- coding: utf-8 -*-
import unittest

from ddby import Money, Currency, get_currency
from ddby.exchange import static

class TestExchange(unittest.TestCase):

    def test_exchanging_currencies(self):
        m = Money(500, 'USD') # $5.00 USD
        rates = {'USD': {'EUR': 1.3}}

        exchange = static.StaticExchange(rates)

        expected = Money(650, 'EUR')

        actual = exchange.exchange_to(m, 'EUR')

        assert expected == actual

    def test_symmetric_exchange(self):
        m = Money(500, 'USD') # $5.00 USD
        rates = {'EUR': {'USD': 0.7}}

        exchange = static.StaticExchange(rates)

        expected = Money(714, 'EUR')

        actual = exchange.exchange_from(m, 'EUR')

        assert expected == actual

    def test_exchanging_precision(self):
        m = Money(500, 'USD') # $5.00 USD
        rates = {'USD': {'JPY': 123.5}}

        exchange = static.StaticExchange(rates)

        expected = Money(618, 'JPY')

        actual = exchange.exchange_to(m, 'JPY')

        assert expected == actual, "Actual {0} != {1}".format(
            expected, actual
            )

    def test_exchanging_precision_from_lower_to_higher_precision(self):
        m = Money(100, 'JPY') # $5.00 USD
        rates = {'JPY': {'USD': 0.01}}

        exchange = static.StaticExchange(rates)

        expected = Money(100, 'USD')

        actual = exchange.exchange_to(m, 'USD')

        assert expected == actual, "Actual {0} != {1}".format(
            expected, actual
            )

    def test_exchanging_precision_from(self):
        m = Money(500, 'USD') # $5.00 USD
        rates = {'JPY': {'USD': 0.01}}

        exchange = static.StaticExchange(rates)

        expected = Money(500, 'JPY')

        actual = exchange.exchange_from(m, 'JPY')

        assert expected == actual, "Actual {0} != {1}".format(
            expected, actual
            )


if __name__ == '__main__':
    unittest.main()
