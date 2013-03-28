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

    

    



if __name__ == '__main__':
    unittest.main()
