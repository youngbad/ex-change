"""Currency amount primitives for the CEMS domain."""

from dataclasses import dataclass
from decimal import Decimal, localcontext


def _add_exact(left: Decimal, right: Decimal) -> Decimal:
    exponent = min(left.as_tuple().exponent, right.as_tuple().exponent)
    precision = max(
        len(left.as_tuple().digits) + left.as_tuple().exponent - exponent,
        len(right.as_tuple().digits) + right.as_tuple().exponent - exponent,
    ) + 1
    with localcontext() as context:
        context.prec = precision
        return left + right


@dataclass(frozen=True)
class Money:
    """An exact amount denominated in one currency.

    Currency-specific precision and rounding are intentionally left to a
    versioned currency catalog and an approved business policy.
    """

    amount: Decimal
    currency: str

    def __post_init__(self):
        if not isinstance(self.amount, Decimal):
            raise TypeError("amount must be a Decimal")
        if not self.amount.is_finite():
            raise ValueError("amount must be finite")
        if not isinstance(self.currency, str) or (
            len(self.currency) != 3
            or not self.currency.isascii()
            or not self.currency.isalpha()
            or not self.currency.isupper()
        ):
            raise ValueError("currency must be a three-letter uppercase code")

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._require_same_currency(other)
        return Money(_add_exact(self.amount, other.amount), self.currency)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        self._require_same_currency(other)
        return Money(
            _add_exact(self.amount, other.amount.copy_negate()), self.currency
        )

    def _require_same_currency(self, other):
        if self.currency != other.currency:
            raise ValueError("cannot combine amounts in different currencies")
