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
        rate = self._scale_rate(rate, money.currency, currency)

        value = int(round(money.get_amount() * rate, 0))

        return Money(value, currency)

    def exchange_from(self, money, currency_code):
        """Perform a symmetric conversion of a Money object to another currency.
        """
        currency = get_currency(currency_code)

        if money.currency == currency:
            return money

        rate = self.get_rate(currency.code, money.currency.code)
        rate = self._scale_rate(rate, currency, money.currency)

        value = int(round(money.get_amount() / rate, 0))

        return Money(value, currency)

    def _scale_rate(self, rate, original, desired):
        """Scale an exchange rate between precisions

        Because ddby stores Money objects at currency precision,
        rather than some arbitrary number of fractional units,
        exchanging between separate currencies can get tricky.

        For instance, let's say we have $5.00 USD, and we want
        to exchange that to Japanese Yen.  The current exchange
        rate is 1 USD = 123.5 JPY.  So we have a Money object
        Money(500, 'USD').  We run the exchange of 500 * 123.5,
        and then make that JPY.  However, this is result:

        500 * 123.5 = 61750 JPY, which is considerably higher
        than the desired 618 JPY we were expecting.

        In order to account for this, we scale the exchange rate
        of 123.5 to be 1.235 to account for the difference in
        precision.

        This now becomes:
        500 * 1.235 = 617.5 JPY, rounded to 618 JPY.
        """
        if original.precision == desired.precision:
            # The two currencies have the same precision, 
            # we can avoid this whole computation
            return rate

        return (rate * pow(10, (desired.precision - original.precision)))

    def get_rate(self, original, desired):
        """Get the rate in order to convert original
        currency to desired currency"""
        raise NotImplementedError

