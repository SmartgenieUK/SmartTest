"""Executable payment-approval example for SmartTest.

Infrastructure stays behind small injected interfaces so the tests can prove
orchestration behaviour without pretending that in-memory teaching code proves
a real payment integration.
"""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


APPROVAL_THRESHOLD = Decimal("10000.00")


class ApprovalUnavailable(RuntimeError):
    """The secondary approval dependency could not return a decision."""


class InvalidAmount(ValueError):
    """The amount is missing, malformed, floating point, or negative."""


class IdempotencyConflict(RuntimeError):
    """An idempotency key was reused for a different payload."""


@dataclass
class PaymentRecord:
    payment_id: str
    amount: Decimal
    initiator_id: str
    state: str


class InMemoryPaymentStore:
    """Inspectable state store for the example, not production storage."""

    def __init__(self):
        self.records = {}

    def save(self, record):
        self.records[record.payment_id] = record

    def get(self, payment_id):
        return self.records[payment_id]


class PaymentApprovalService:
    def __init__(self, approval_gateway, execution_gateway, audit_sink, store=None):
        self._approval_gateway = approval_gateway
        self._execution_gateway = execution_gateway
        self._audit_sink = audit_sink
        self._store = store or InMemoryPaymentStore()
        self._idempotent_results = {}

    @staticmethod
    def _parse_amount(amount):
        if amount is None or isinstance(amount, (float, bool)):
            raise InvalidAmount(amount)
        try:
            parsed = Decimal(amount)
        except (InvalidOperation, TypeError, ValueError):
            raise InvalidAmount(amount) from None
        if not parsed.is_finite() or parsed < 0:
            raise InvalidAmount(amount)
        return parsed

    @classmethod
    def requires_secondary_approval(cls, amount):
        return cls._parse_amount(amount) >= APPROVAL_THRESHOLD

    def _once(self, operation, idempotency_key, fingerprint, action):
        key = (operation, idempotency_key)
        existing = self._idempotent_results.get(key)
        if existing is not None:
            previous_fingerprint, result = existing
            if previous_fingerprint != fingerprint:
                raise IdempotencyConflict(idempotency_key)
            return result
        result = action()
        self._idempotent_results[key] = (fingerprint, result)
        return result

    def submit(self, payment_id, amount, *, initiator_id, idempotency_key):
        parsed = self._parse_amount(amount)
        fingerprint = (payment_id, str(parsed), initiator_id)

        def submit_once():
            if self.requires_secondary_approval(parsed):
                record = PaymentRecord(
                    payment_id, parsed, initiator_id, "APPROVAL_PENDING"
                )
                self._store.save(record)
                self._approval_gateway.request(payment_id)
                return record.state

            record = PaymentRecord(payment_id, parsed, initiator_id, "EXECUTED")
            self._store.save(record)
            self._execution_gateway.execute(payment_id)
            return record.state

        return self._once("submit", idempotency_key, fingerprint, submit_once)

    def approve(
        self,
        payment_id,
        *,
        approver_id,
        approver_is_authorized,
        idempotency_key,
    ):
        fingerprint = (payment_id, approver_id, approver_is_authorized)

        def approve_once():
            record = self._store.get(payment_id)
            if record.state != "APPROVAL_PENDING":
                return record.state

            if approver_id == record.initiator_id or not approver_is_authorized:
                self._audit_sink.record(
                    "APPROVAL_REJECTED",
                    payment_id,
                    approver_id,
                    "INITIATOR" if approver_id == record.initiator_id else "UNAUTHORIZED",
                )
                return record.state

            try:
                approved = self._approval_gateway.approve(payment_id, approver_id)
            except ApprovalUnavailable:
                self._audit_sink.record(
                    "APPROVAL_ERROR", payment_id, approver_id, "DEPENDENCY_UNAVAILABLE"
                )
                return record.state

            if not approved:
                record.state = "APPROVAL_REJECTED"
                self._store.save(record)
                self._audit_sink.record(
                    "APPROVAL_REJECTED", payment_id, approver_id, "GATEWAY_REJECTED"
                )
                return record.state

            record.state = "EXECUTED"
            self._store.save(record)
            self._audit_sink.record(
                "APPROVAL_ACCEPTED", payment_id, approver_id, "AUTHORIZED"
            )
            self._execution_gateway.execute(payment_id)
            return record.state

        return self._once("approve", idempotency_key, fingerprint, approve_once)

    def state(self, payment_id):
        return self._store.get(payment_id).state
