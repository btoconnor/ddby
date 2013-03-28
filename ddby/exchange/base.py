from ..currency import get_currency
from ..money import Money

__all__ = ['Exchange']

class Exchange(object):
    """Represents a money exchange.

    This exchanges a Money object from one currency to/from
    another currency.  This is done by extending this class,
    and implementing a `get_rate` function that returns an exchange
    rate from one currency to another.
    """
    def exchange_to(self, money, currency_code):
        """Exchange a money object to another currency
        """
        currency = get_currency(currency_code)

        # Instead of doing a lot of math, let's do this check first
        if money.currency == currency:
            return money

        rate = self.get_rate(money.currency.code, currency.code)

        value = int(round(money.amount * rate, 0))

        return Money(value, currency)

    def exchange_from(self, money, currency_code):
        """Perform a symmetric conversion of a Money object to another currency.
        """
        currency = get_currency(currency_code)

        if money.currency == currency:
            return money

        rate = self.get_rate(currency.code, money.currency.code)

        value = int(round(money.amount / rate, 0))

        return Money(value, currency)

    def get_rate(self, original, desired):
        """Get the rate in order to convert original
        currency to desired currency"""
        raise NotImplementedError
