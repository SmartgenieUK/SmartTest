"""Minimal payment-approval policy used by the SmartTest executable example."""

from decimal import Decimal


APPROVAL_THRESHOLD = Decimal("10000.00")


class ApprovalUnavailable(RuntimeError):
    """The secondary approval dependency could not return a decision."""


class DuplicateDecision(RuntimeError):
    """A payment already has a recorded approval decision."""


class PaymentApprovalService:
    def __init__(self, approval_gateway):
        self._approval_gateway = approval_gateway
        self._decided_payment_ids = set()

    @staticmethod
    def requires_secondary_approval(amount):
        return Decimal(amount) >= APPROVAL_THRESHOLD

    def decide(self, payment_id, amount, *, approver_is_authorized=False):
        if not self.requires_secondary_approval(amount):
            return "APPROVED"

        if not approver_is_authorized:
            return "BLOCKED_UNAUTHORIZED"

        if payment_id in self._decided_payment_ids:
            raise DuplicateDecision(payment_id)

        try:
            approved = self._approval_gateway.approve(payment_id)
        except ApprovalUnavailable:
            return "PENDING_APPROVAL"

        self._decided_payment_ids.add(payment_id)
        return "APPROVED" if approved else "REJECTED"
