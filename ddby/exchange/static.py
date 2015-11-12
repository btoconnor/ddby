from .base import Exchange

__all__ = ['StaticExchange']


class StaticExchange(Exchange):

    def __init__(self, values):
        """Establish an exchange of static rates

        The format of the values list is a 2-dimensional
        array of original currency -> desired currency

        An example:
        values = {'USD': {'GBP': 1.5, 'EUR': 1.3},
                  'GBP': {'USD': 0.7, 'EUR': 0.9},
                  'EUR': {'USD': 0.8, 'GBP': 1.1}
                 }

        The above example would provide exchange rates for
        converting money between EUR, GBP, and USD.
        """
        self.values = values

    def get_rate(self, original, desired):
        """Get the rate in order to convert original
        currency to desired currency"""
        return self.values[original][desired]
