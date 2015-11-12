import unittest

from ddby import Money

class TestMoneyComparison(unittest.TestCase):
    "Covers the functions that override comparison operators"

    def test_lesser_value_is_less_than_another(self):
        m1 = Money(100, 'USD')

        m2 = Money(200, 'USD')

        assert m1 < m2

    def test_greater_value_is_not_less_than_another(self):
        m1 = Money(300, 'USD')

        m2 = Money(200, 'USD')

        assert not m1 < m2

    def test_equal_value_is_not_less_than_another(self):
        m1 = Money(200, 'USD')

        m2 = Money(200, 'USD')

        assert not m1 < m2

    def test_equal_value_is_gte(self):
        m1 = Money(200, 'USD')
        assert m1 >= m1

    def test_greater_value_is_gte(self):
        m1 = Money(200, 'USD')
        m2 = Money(300, 'USD')

        assert m2 >= m1

    def test_equal_value_is_lte(self):
        m1 = Money(200, 'USD')
        assert m1 >= m1

    def test_less_value_is_lte(self):
        m1 = Money(200, 'USD')
        m2 = Money(300, 'USD')

        assert m1 <= m2

    def test_values_differing_by_fractional_amounts_are_not_equal(self):
        m1 = Money(400, 'USD')
        m2 = Money(40001, 'USD', 4)

        assert m1 != m2, "Values with fractions of a penny are not equal"

    def test_values_equal_but_different_precisions_are_still_equal(self):
        m1 = Money(400, 'USD')
        m2 = Money(40000, 'USD', 4)

        assert m1 == m2, \
            "Values that are equivalent but of different precisions are still equal"

    def test_materialized_amounts_are_less_than_amounts_with_fractions(self):
        m1 = Money(400, 'USD')
        m2 = Money(40001, 'USD', 4)

        assert m1 < m2

    def test_fractional_amounts_are_greater_than_materialized(self):
        m1 = Money(400, 'USD')
        m2 = Money(40001, 'USD', 4)

        assert m2 > m1

    def test_fractional_equivalents_are_equivalent(self):
        m1 = Money(40001, 'USD', 4)
        m2 = Money(40001, 'USD', 4)

        assert m1 == m2

    def test_varying_fractional_amounts_less_than(self):
        m1 = Money(40000001, 'USD', 4)
        m2 = Money(4000001, 'USD', 3)

        assert m1 < m2

    def test_varying_fractional_amounts_greater_than(self):
        m1 = Money(40000101, 'USD', 3)
        m2 = Money(4000002, 'USD', 2)

        assert m1 > m2

    def test_comparing_different_currencies_raises_error(self):
        m1 = Money(4000, 'USD')
        m2 = Money(4000, 'EUR')

        self.assertRaises(ValueError, m1.__lt__, m2)


if __name__ == '__main__':
    unittest.main()
