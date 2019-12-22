# -*- coding: utf-8 -*-
__all__ = ['get_currency', 'Currency']

_CURRENCIES = {}


def get_currency(currency_code):
    "Retrieve currency by the ISO currency code."
    return _CURRENCIES[currency_code]


class Currency:
    "Class representing a currency, such as USD, or GBP"

    __slots__ = ['code', 'name', 'symbol', 'precision']

    def __init__(self, code, name, symbol, precision):
        self.code = code
        self.name = name
        self.symbol = symbol
        self.precision = precision

    def __str__(self):
        return "{0}, {1}, {2}".format(self.name, self.code, self.symbol).encode('utf-8')

    def __repr__(self):
        return "Currency<{0}, {1}, {2}>".format(self.name, self.code, self.symbol).encode('utf-8')

    def __eq__(self, o):
        return self.code == o.code

    def __ne__(self, o):
        return not self == o

# TODO: Add more currencies from ISO 4217

_CURRENCIES['AUD'] = Currency('AUD', 'Australian Dollar', "$", 2)
_CURRENCIES['BRL'] = Currency('BRL', 'Brazilian Real', "R$", 2)
_CURRENCIES['CAD'] = Currency('CAD', 'Canadian Dollar', "$", 2)
_CURRENCIES['CHF'] = Currency('CHF', 'Swiss Franc', "CHF", 2)
_CURRENCIES['CZK'] = Currency('CZK', 'Czech Koruna', "K\u010d", 2)
_CURRENCIES['EUR'] = Currency('EUR', 'Euro', "\u20AC", 2)
_CURRENCIES['GBP'] = Currency('GBP', 'Pound Sterling', "\u00A3", 2)
_CURRENCIES['ILS'] = Currency('ILS', 'Israel Shekel', "\u20AA", 2)
_CURRENCIES['JPY'] = Currency('JPY', 'Yen', '\u00A5', 0)
_CURRENCIES['MXN'] = Currency('MXN', 'Mexican Peso', "$", 2)
_CURRENCIES['NZD'] = Currency('NZD', 'New Zealand Dollar', "$", 2)
_CURRENCIES['USD'] = Currency('USD', 'United States Dollar', '$', 2)
