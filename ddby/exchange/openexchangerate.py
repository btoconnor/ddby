from .base import Exchange

__all__ = ['Exchange']

class OpenExchangeRate(Exchange):

    def exchange_to(self, money, currency_code):
        currency = get_currency(currency_code)

        # Instead of doing a lot of math, let's do this check first
        if (money.currency == currency):
            return money

        rate = self.get_rate(money.currency, currency)

        return Money(money.amount * rate, currency)

    def exchange_from(self, money, currency_code):
        pass

    def get_rate(self, original, desired):
        """Get the rate in order to convert original
        currency to desired currency"""
        raise NotImplementedError
