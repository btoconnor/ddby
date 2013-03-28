# -*- coding: utf-8 -*-
__all__ = ['get_currency', 'Currency']

_CURRENCIES = {}

def get_currency(currency_code):
    return _CURRENCIES[currency_code]

class Currency(object):
    "Class representing a currency, such as USD, or GBP"

    def __init__(self, code, name, symbol, precision):
        self.code = code
        self.name = name
        self.symbol = symbol
        self.precision = precision

    def __unicode__(self):
        return u"{0}, {1}, {2}".format(self.name, self.code, self.symbol)

    def __str__(self):
        return u"{0}, {1}, {2}".format(self.name, self.code, self.symbol).encode('utf-8')

    def __repr__(self):
        return u"Currency<{0}, {1}, {2}>".format(self.name, self.code, self.symbol).encode('utf-8')

    def __eq__(self, o):
        return self.code == o.code

    def __ne__(self, o):
        return not (self == o)

# TODO: Add more currencies from ISO 4217

_CURRENCIES[u'AUD'] = Currency(u'AUD', u'Australian Dollar', u"$", 2)
_CURRENCIES[u'CAD'] = Currency(u'CAD', u'Canadian Dollar', u"$", 2)
_CURRENCIES[u'EUR'] = Currency(u'EUR', u'Euro', u"\u20AC", 2)
_CURRENCIES[u'GBP'] = Currency(u'GBP', u'Pound Sterling', u"\u00A3", 2)
_CURRENCIES[u'JPY'] = Currency(u'JPY', u'Yen', u'\u00A5', 0) 
_CURRENCIES[u'USD'] = Currency(u'USD', u'United States Dollar', u'$', 2)
