from .base import Exchange

__all__ = ['StaticExchange']

class StaticExchange(Exchange):

    def __init__(self, values):
        "Grab rates from an array"
        self.values = values

    def get_rate(self, original, desired):
        """Get the rate in order to convert original
        currency to desired currency"""
        return self.values[original][desired]
