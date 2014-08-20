# ddby library for representing and working with money in Python

This library provides a simple way for representing and dealing with money in python.

ddby internally represents money as integers, making it easy to store in databases and port to other applications.

[![Build Status](https://travis-ci.org/btoconnor/ddby.svg?branch=master)](https://travis-ci.org/btoconnor/ddby)

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

### Fractional amounts
In certain applications, it makes sense to deal with monetary values in fractions
of a whole value.  For instance, you might have $50.005 USD, and when you add that to
$30.005 USD, you would want to get $80.01 USD.  ddby supports arbitrary precision on
Money objects, which allows you to represent these fractional values with an optional
precision argument.

Example:

```python
>>> from ddby import Money
>>> m1 = Money(50005, 'USD', precision=3) # We've got 3 precision units rather than a standard 2 for USD
>>> m2 = Money(30005, 'USD', precision=3)
>>> m3 = m1 + m2
>>> print m3.materialize()
'$80.01 USD'
```

Materializing a Money object will return a new Money object with any fractional values rounded
away to the nearest whole value of a currency.

Example:

```python
>>> m1 = Money(50002, 'USD', precision=3)
>>> m2 = Money(30002, 'USD', precision=3)
>>> m3 = m1 + m2
>>> print m3.materialize()
'$80.00 USD'
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
'€6.50 EUR'
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

## License

The MIT License (MIT)

Copyright 2014 Brian O'Connor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
