# -*- coding: utf-8 -*-
from .money import Money
from .error import IncorrectSerializeFormat

class Serializer(object):
    """Serialize a Money object for sending over the wire.

    It is not recommended to use the utility of this class
    to store in the database.  This would prevent you from
    doing anything with aggregate functions in SQL, such
    as SUM, MAX, MIN, etc.  Chances are, it's not worth the
    trouble.  This is really so that you can exchange
    monetary values between stacks that communicate over
    network protocols.

    Note: precision is included in anticipation of 
    arbitrary precision which is planned in the near future.
    """
    VERSION = 1

    def serialize(self, money):
        "Convert a money object into a serialized value"
        return "{0}:{1}:{2}:{3}".format(
            self.VERSION,
            money.precise_amount,
            money.currency.code,
            money.precision
        )

    def unserialize(self, money_string):
        "Given a string, return a money object that it represents."
        results = money_string.split(':')
        if len(results) != 4:
            raise IncorrectSerializeFormat("String {0} is of incorrect format to parse".format(money_string))

        try:
            amount = int(results[1])
        except ValueError:
            raise IncorrectSerializeFormat("Amount {0} is not an integer".format(results[1]))

        version, amount, currency_code, precision = results

        return Money(
            int(amount),
            currency_code,
            precision=int(precision)
        )
            
