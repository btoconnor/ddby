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


if __name__ == '__main__':
    unittest.main()

