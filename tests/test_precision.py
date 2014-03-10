# -*- coding: utf-8 -*-
import unittest

from ddby import Money

class TestPrecision(unittest.TestCase):

    def test_rounding_to_currency_precision(self):
        m1 = Money(40000, 'USD', 4)

        rounded = m1.round_to(2)

        assert rounded.get_amount() == 400
        assert rounded.precise_amount == 400
        assert rounded.precision == 2

    def test_lifting_precision(self):
        m1 = Money(400, 'USD')

        lifted = m1.round_to(4)

        assert lifted.precise_amount == 40000, \
            "Precise amount {0} is not equal to 40000".format(m1.precise_amount)

        assert lifted == m1, \
            "Currency amount {0} is not equal to 400".format(lifted.get_amount())

    def test_highest_precision_with_lifted_money(self):
        m1 = Money(400, 'USD')
        m2 = Money(40000, 'USD', 4)

        assert Money.highest_precision(m1, m2) == 4

    def test_exception_throw_when_rounding_to_lower_precision_than_currency(self):
        m1 = Money(400, 'USD')

        self.assertRaises(ValueError, m1.round_to, 1)

    def test_materialized_fractional_amounts(self):
        m1 = Money(400, 'USD')
        m2 = Money(40001, 'USD', 4)

        assert m2.materialize() == m1

    def test_adding_fractional_values(self):
        m1 = Money(50005, 'USD', precision=3)
        m2 = Money(30005, 'USD', precision=3)
        expected = Money(80010, 'USD', precision=3)

        actual = m1 + m2
        assert actual == expected

    def test_materializing_after_addition(self):
        m1 = Money(50005, 'USD', precision=3)
        m2 = Money(30005, 'USD', precision=3)
        expected = Money(8001, 'USD')

        m3 = m1 + m2
        actual = m3.materialize()

        assert actual == expected

    def test_materializing_rounds_away_fractional_amount(self):
        m1 = Money(50002, 'USD', precision=3)
        m2 = Money(30002, 'USD', precision=3)

        m3 = m1 + m2
        expected = Money(8000, 'USD')
        actual = m3.materialize()

        assert actual == expected
        

if __name__ == '__main__':
    unittest.main()
