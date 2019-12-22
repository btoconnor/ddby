# -*- coding: utf-8 -*-
from __future__ import division

from .currency import get_currency

__all__ = ['Money']


class Money:
    "An object representing money"

    __slots__ = ['precise_amount', 'currency', 'precision']

    def __init__(self, amount, currency, precision=None):
        if isinstance(currency, str):
            # Currency code was passed in.  Go look it up.
            currency = get_currency(currency)

        self.currency = currency

        if precision:
            self.precision = precision
        else:
            self.precision = self.currency.precision

        self.precise_amount = self._get_amount(amount, self.precision)

    def get_inverse(self):
        """Return a Money object with amount inverted.

        If the amount is positive, this will return a negative amount,
        and if the amount is negative, this will return a positive amount.
        """
        return Money(-self.precise_amount, self.currency, self.precision)

    def get_amount(self):
        "Returns a materialized amount represented by this money object."
        return self.materialize().precise_amount

    def materialize(self):
        """Returns a money object that has been rounded to the natural
        precision level of the currency it represents.
        """
        return self.round_to(self.currency.precision)

    # Override functions to cast to data types
    def __int__(self):
        """Cast the Money object to an int

        This cast will materialize the Money object to currency precision.
        """
        return self.get_amount()

    def __float__(self):
        """Cast the Money object to a float

        This cast will materialize the Money object to currency precision.
        """
        return round(
            float(self.get_amount()) / pow(10, self.currency.precision),
            self.currency.precision
        )

    def round_to(self, precision_level):
        """Return a Money object that is rounded to the specified
        level of precision.

        This will throw an ValueError if you attempt
        to round a money object to a precision that is lower than
        the currency in which it is representing.  For instance,
        if you try and round a USD monetary value to precision level 1,
        that doesn't make any sense, and this will raise an exception
        as a result.
        """
        if precision_level < self.currency.precision:
            raise ValueError("Cannot round to a precision less than the currency precision")

        if precision_level == self.precision:
            return self

        scale_factor = precision_level - self.precision

        new_amount = int(round(self.precise_amount * pow(10, scale_factor)))

        return Money(new_amount, self.currency, precision_level)

    @classmethod
    def highest_precision(cls_, *args):
        return max([x.precision for x in args])

    @classmethod
    def normalize_precisions(cls_, *args):
        precision = cls_.highest_precision(*args)

        return [x.round_to(precision) for x in args]

    # Override numeric operations
    def __add__(self, other):
        self._assert_same_currency(other.currency)
        a, b = Money.normalize_precisions(self, other)

        return Money(a.precise_amount + b.precise_amount,
                     a.currency, a.precision)

    def __sub__(self, other):
        self._assert_same_currency(other.currency)
        a, b = Money.normalize_precisions(self, other)

        return Money(a.precise_amount - b.precise_amount,
                     self.currency, a.precision)

    def __mul__(self, amount):
        return Money(self.precise_amount * amount, self.currency, self.precision)

    def __rmul__(self, amount):
        return Money(self.precise_amount * amount, self.currency, self.precision)

    def __truediv__(self, amount):
        return Money(int(self.precise_amount / amount), self.currency, self.precision)

    def __eq__(self, other):
        if self.currency != other.currency:
            return False

        a, b = Money.normalize_precisions(self, other)

        return (a.precise_amount == b.precise_amount)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        self._assert_same_currency(other.currency)
        a, b = Money.normalize_precisions(self, other)

        return (a.precise_amount < b.precise_amount)

    def __gt__(self, other):
        self._assert_same_currency(other.currency)
        a, b = Money.normalize_precisions(self, other)

        return (a.precise_amount > b.precise_amount)

    def __le__(self, other):
        self._assert_same_currency(other.currency)
        a, b = Money.normalize_precisions(self, other)

        return (a.precise_amount <= b.precise_amount)

    def __ge__(self, other):
        self._assert_same_currency(other.currency)
        a, b = Money.normalize_precisions(self, other)

        return (a.precise_amount >= b.precise_amount)

    def __str__(self):
        return "{0}{1:.2f} {2}".format(
            self.currency.symbol,
            float(self), self.currency.code
        ).encode('utf-8')

    def __repr__(self):
        return "Money<{0}, {1}, {2}>".format(
            self.precise_amount,
            self.currency.code,
            self.precision
        ).encode('utf-8')

    def __bool__(self):
        return bool(self.precise_amount)

    # Helper functions
    def _assert_same_currency(self, currency):
        if self.currency != currency:
            raise ValueError("Currencies are not the same")

    def _get_amount(self, amount, precision):
        if isinstance(amount, int):
            return amount
        elif isinstance(amount, float):
            return int(amount * pow(10, precision))
        else:
            raise ValueError("Amount is not an int or float")
