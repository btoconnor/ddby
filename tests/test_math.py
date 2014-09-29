import unittest

from ddby import Money

class TestMoney(unittest.TestCase):

    def test_adding_two_monies(self):
        m1 = Money(500, 'USD')
        m2 = Money(200, 'USD')

        actual = m1 + m2
        expected = Money(700, 'USD')

        assert actual == expected

    def test_subtracting_two_monies(self):
        m1 = Money(500, 'USD')
        m2 = Money(200, 'USD')

        actual = m1 - m2
        expected = Money(300, 'USD')

        assert actual == expected

    def test_adding_two_monies_of_different_precision(self):
        m1 = Money(340, 'USD')
        m2 = Money(4501, 'USD', 3)

        expected = Money(7901, 'USD', 3)
        actual = m1 + m2

        assert actual.precise_amount == expected.precise_amount
        assert actual.precision == expected.precision

    def test_subtracting_two_monies_of_different_precision(self):
        m1 = Money(4501, 'USD', 3)
        m2 = Money(340, 'USD')

        expected = Money(1101, 'USD', 3)
        actual = m1 - m2

        assert actual.precise_amount == expected.precise_amount
        assert actual.precision == expected.precision

    def test_multipying_a_money_object(self):
        m1 = Money(4500, 'USD')
        m_amount = 2
        
        expected = Money(9000, 'USD')

        actual = m1 * m_amount

        assert actual == expected

    def test_dividing_a_money_object(self):
        m1 = Money(9000, 'USD')
        m_amount = 2
        
        expected = Money(4500, 'USD')

        actual = m1 / m_amount

        assert actual == expected, "Actual not equal to expected: {0} :: {1}".format(actual, expected)

    def test_iadd(self):
        m1 = Money(9000, 'USD')
        add_amount = Money(3000, 'USD')

        expected = Money(12000, 'USD')
        m1 += add_amount
        assert m1 == expected

    def test_rmultiply(self):
        m1 = Money(4500, 'USD')
        m_amount = 2
        expected = Money(9000, 'USD')
        actual = m_amount * m1

        assert actual == expected

if __name__ == '__main__':
    unittest.main()

