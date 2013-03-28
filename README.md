# ddby library for representing and working with money in Python

This library provides a simple way for representing and dealing with money in python.

ddby internally represents money as integers, making it easy to store in databases and port to other applications.

Example:

```python
>>> from ddby import Money
>>> m = Money(500, 'USD') # $5.00 USD

>>> print int(m)
500
>>> print float(m)
5.0
```

It's important to note that casting a Money object to int / float is not transitive.  For instance,

```python
>>> int(m) == float(m)
False
```

However, instantiating a Money object around each of these casts is transitive:

```python
>>> Money(int(m), m.currency) == Money(float(m), m.currency)
True
```

### Exchanging currencies
ddby makes it easy to exchange money from one currency to another with the notion of an 'exchange'.

The ability to exchange currencies with static rates is provided in the library.

Example:

```python
>>> from ddby import Money, Currency
>>> from ddby.exchange import static

>>> rates = {'USD': {'EUR': 1.3}} # rate to convert USD to EUR
>>> m = Money(500, 'USD') # $5.00 USD
>>> exchange = static.StaticExchange(rates)

>>> print exchange.exchange_to(m, 'EUR')
€6.50 EUR
```

### Making your own exchange
For all but the most trivial applications, a static exchange is not suitable.  ddby makes it trivial to provide an interface
to make your own exchange.  Simply subclass the Exchange object from ddby.exchange.base and implement a ```get_rate``` method
which returns the rate from original -> desired.  From there, you can instantiate your new exchange and call ```exchange_to()```
or ```exchange_from()```

Example:

```python
# The worst currency exchange in the world:
from ddby.exchange.base import Exchange

class MyExchange(Exchange):
    def get_rate(self, original, desired):
        return 1.0
```


This exchange would simply convert 1 for 1 of every currency in the world.  Not terribly applicable, but it illustrates how
easy it is to implement your own exchange, either from a database, a web api, or a random number generator.
