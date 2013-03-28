# ddby library for representing and working with money in Python

This library provides a simple way for representing and dealing with money in python.

ddby internally represents money as integers (not Decimal objects).

Example:
    from ddby import Money
    m = Money(500, 'USD')

    print int(m)
    print float(m)

### Exchanging currencies
ddby makes it easy to exchange money from one currency to another.

The ability to exchange currencies with static rates is provided in the package.

Example:
    from ddby import Money, Currency
    from ddby.exchange import static

    rates = {'USD': {'EUR': 1.3}} # rate to convert USD to EUR
    m = Money(500, 'USD') # $5.00 USD
    exchange = static.StaticExchange(rates)

    print exchange->exchange_to(m, 'EUR')
    >>> €6.50 EUR

If you want to make your own exchange based off more dynamic values (such as from a database), it's trivial to do so.

Simple subclass exchange.base Exchange and implement a get_rate method which returns the exchange rate from original to desired.

    