from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 5)

        self.assertEquals(res, 5)
