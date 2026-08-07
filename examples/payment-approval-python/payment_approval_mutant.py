"""Deliberately faulty boundary mutant; use only to demonstrate test sensitivity."""

from decimal import Decimal

from payment_approval import (
    APPROVAL_THRESHOLD,
    ApprovalUnavailable,
    DuplicateDecision,
    PaymentApprovalService as CorrectService,
)


class PaymentApprovalService(CorrectService):
    @staticmethod
    def requires_secondary_approval(amount):
        # Deliberate defect: the requirement says “£10,000 or more”.
        return Decimal(amount) > APPROVAL_THRESHOLD

__all__ = [
    "ApprovalUnavailable",
    "DuplicateDecision",
    "PaymentApprovalService",
]
