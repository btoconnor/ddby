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

        print actual

        assert expected == actual


if __name__ == '__main__':
    unittest.main()
