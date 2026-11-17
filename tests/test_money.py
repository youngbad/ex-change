import unittest
from decimal import Decimal

from backend.cems.domain.money import Money


class MoneyTests(unittest.TestCase):
    def test_add_and_subtract_preserve_exact_decimal_amounts(self):
        first = Money(Decimal("10.125"), "PLN")
        second = Money(Decimal("0.005"), "PLN")

        self.assertEqual((first + second).amount, Decimal("10.130"))
        self.assertEqual((first - second).amount, Decimal("10.120"))

    def test_large_amount_addition_is_not_rounded_by_decimal_context(self):
        first = Money(Decimal("123456789012345678901234567890.12"), "PLN")
        second = Money(Decimal("0.01"), "PLN")

        self.assertEqual(
            (first + second).amount,
            Decimal("123456789012345678901234567890.13"),
        )
        self.assertEqual(
            (
                Money(Decimal("123456789012345678901234567890.13"), "PLN")
                - first
            ).amount,
            Decimal("0.01"),
        )

    def test_rejects_float_amount(self):
        with self.assertRaises(TypeError):
            Money(0.1, "PLN")

    def test_rejects_non_finite_amount(self):
        with self.assertRaises(ValueError):
            Money(Decimal("NaN"), "PLN")

    def test_rejects_invalid_currency_code(self):
        for currency in ("pln", "EU", "1PL", "PLN ", None):
            with self.subTest(currency=currency):
                with self.assertRaises(ValueError):
                    Money(Decimal("1"), currency)

    def test_rejects_arithmetic_between_currencies(self):
        with self.assertRaises(ValueError):
            Money(Decimal("1"), "PLN") + Money(Decimal("1"), "EUR")


if __name__ == "__main__":
    unittest.main()
