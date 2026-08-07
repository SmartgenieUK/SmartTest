"""Deliberately faulty boundary mutant; use only for sensitivity evidence."""

from payment_approval import *  # noqa: F401,F403 - re-export teaching API
from payment_approval import APPROVAL_THRESHOLD, PaymentApprovalService as CorrectService


class PaymentApprovalService(CorrectService):
    @classmethod
    def requires_secondary_approval(cls, amount):
        # Deliberate defect: exactly GBP 10,000 incorrectly bypasses approval.
        return cls._parse_amount(amount) > APPROVAL_THRESHOLD
