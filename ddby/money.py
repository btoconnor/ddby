# -*- coding: utf-8 -*-
from .error import InvalidOperationException
from .currency import get_currency

__all__ = ['Money']

class Money(object):
    "An object representing money"

    def __init__(self, amount, currency):        
        if isinstance(currency, basestring):
            # Currency code was passed in.  Go look it up.
            currency = get_currency(currency)

        self.amount = self._get_amount(amount, currency.precision)
        self.currency = currency

    def get_inverse(self):
        """Return a Money object with amount inverted.

        If the amount is positive, this will return a negative amount,
        and if the amount is negative, this will return a positive amount.
        """
        return Money(-self.amount, self.currency)

    # Override functions to cast to data types
    def __int__(self):
        "Cast the Money object to an int"
        return self.amount

    def __float__(self):
        "Cast the Money object to a float"
        # TODO: make sure the rounding is proper based on precision
        return round(
            float(self.amount) / pow(10, self.currency.precision),
            self.currency.precision)

    # Override numeric operations
    def __add__(self, other):
        if isinstance(other, Money):
            self._assert_same_currency(other.currency)
            
            return Money(
                self.amount + other.amount, self.currency
                )

        amount = self._get_amount(other, self.currency.precision)
        return Money(self.amount + amount, self.currency)

    def __sub__(self, other):
        if isinstance(other, Money):
            self._assert_same_currency(other.currency)
            
            return Money(
                self.amount - other.amount, self.currency
                )

        amount = self._get_amount(other, self.currency.precision)
        return Money(self.amount - amount, self.currency)

    def __eq__(self, other):
        self._assert_same_currency(other.currency)
        return (self.amount == other.amount)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        self._assert_same_currency(other.currency)
        return (self.amount < other.amount)
    
    def __gt__(self, other):
        self._assert_same_currency(other.currency)
        return (self.amount > other.amount)

    def __lte__(self, other):
        self._assert_same_currency(other.currency)
        return (self.amount <= other.amount)
 
    def __gte__(self, other):
        self._assert_same_currency(other.currency)
        return (self.amount >= other.amount)

    def __str__(self):
        return u"{0}{1:.2f} {2}".format(
            self.currency.symbol,
            float(self), self.currency.code
            ).encode('utf-8')
    
    def __unicode__(self):
        return u"{0}{1:.2f} {2}".format(
            self.currency.symbol,
            float(self), self.currency.code
            )

    def __repr__(self):
        return u"Money<{0}, {1}>".format(
            self.amount,
            self.currency.code
            ).encode('utf-8')

    def __nonzero__(self):
        return bool(self.amount)

    # Helper functions
    def _assert_same_currency(self, currency):
        if self.currency != currency:
            raise InvalidOperationException("Currencies are not the same")

    def _get_amount(self, amount, precision):
        if isinstance(amount, int):
            return amount
        elif isinstance(amount, float):
            return int(amount * pow(10, precision))
        else:
            raise InvalidOperationException("Amount is not an int or float")
            
