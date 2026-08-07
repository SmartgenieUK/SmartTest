import importlib
import os
import unittest


policy = importlib.import_module(
    os.environ.get("SMARTTEST_PAYMENT_MODULE", "payment_approval")
)


class StubApprovalGateway:
    def __init__(self, result=True, unavailable=False):
        self.result = result
        self.unavailable = unavailable
        self.requests = []
        self.decisions = []

    def request(self, payment_id):
        self.requests.append(payment_id)

    def approve(self, payment_id, approver_id):
        self.decisions.append((payment_id, approver_id))
        if self.unavailable:
            raise policy.ApprovalUnavailable("approval dependency unavailable")
        return self.result


class StubExecutionGateway:
    def __init__(self):
        self.calls = []

    def execute(self, payment_id):
        self.calls.append(payment_id)


class StubAuditSink:
    def __init__(self):
        self.events = []

    def record(self, event, payment_id, actor_id, reason):
        self.events.append((event, payment_id, actor_id, reason))


class PaymentApprovalTests(unittest.TestCase):
    def service(self, *, result=True, unavailable=False):
        approval = StubApprovalGateway(result=result, unavailable=unavailable)
        execution = StubExecutionGateway()
        audit = StubAuditSink()
        service = policy.PaymentApprovalService(approval, execution, audit)
        return service, approval, execution, audit

    def test_below_threshold_executes_without_approval_request(self):
        service, approval, execution, _ = self.service()
        result = service.submit(
            "p-1", "9999.99", initiator_id="maker", idempotency_key="submit-1"
        )
        self.assertEqual("EXECUTED", result)
        self.assertEqual([], approval.requests)
        self.assertEqual(["p-1"], execution.calls)

    def test_exact_threshold_waits_for_distinct_authorized_approval(self):
        service, approval, execution, audit = self.service()
        submitted = service.submit(
            "p-2", "10000.00", initiator_id="maker", idempotency_key="submit-2"
        )
        self.assertEqual("APPROVAL_PENDING", submitted)
        self.assertEqual(["p-2"], approval.requests)
        self.assertEqual([], execution.calls)

        approved = service.approve(
            "p-2",
            approver_id="checker",
            approver_is_authorized=True,
            idempotency_key="approve-2",
        )
        self.assertEqual("EXECUTED", approved)
        self.assertEqual([("p-2", "checker")], approval.decisions)
        self.assertEqual(["p-2"], execution.calls)
        self.assertEqual(
            [("APPROVAL_ACCEPTED", "p-2", "checker", "AUTHORIZED")], audit.events
        )

    def test_above_threshold_gateway_rejection_does_not_execute(self):
        service, approval, execution, _ = self.service(result=False)
        service.submit(
            "p-3", "10000.01", initiator_id="maker", idempotency_key="submit-3"
        )
        result = service.approve(
            "p-3",
            approver_id="checker",
            approver_is_authorized=True,
            idempotency_key="approve-3",
        )
        self.assertEqual("APPROVAL_REJECTED", result)
        self.assertEqual([("p-3", "checker")], approval.decisions)
        self.assertEqual([], execution.calls)

    def test_initiator_approval_is_rejected_audited_and_left_pending(self):
        service, approval, execution, audit = self.service()
        service.submit(
            "p-4", "12000", initiator_id="maker", idempotency_key="submit-4"
        )
        result = service.approve(
            "p-4",
            approver_id="maker",
            approver_is_authorized=True,
            idempotency_key="approve-4",
        )
        self.assertEqual("APPROVAL_PENDING", result)
        self.assertEqual([], approval.decisions)
        self.assertEqual([], execution.calls)
        self.assertEqual(
            [("APPROVAL_REJECTED", "p-4", "maker", "INITIATOR")], audit.events
        )

    def test_unauthorized_approval_is_rejected_audited_and_left_pending(self):
        service, approval, execution, audit = self.service()
        service.submit(
            "p-5", "12000", initiator_id="maker", idempotency_key="submit-5"
        )
        result = service.approve(
            "p-5",
            approver_id="observer",
            approver_is_authorized=False,
            idempotency_key="approve-5",
        )
        self.assertEqual("APPROVAL_PENDING", result)
        self.assertEqual([], approval.decisions)
        self.assertEqual([], execution.calls)
        self.assertEqual(
            [("APPROVAL_REJECTED", "p-5", "observer", "UNAUTHORIZED")],
            audit.events,
        )

    def test_dependency_failure_is_audited_pending_and_never_executed(self):
        service, approval, execution, audit = self.service(unavailable=True)
        service.submit(
            "p-6", "12000", initiator_id="maker", idempotency_key="submit-6"
        )
        result = service.approve(
            "p-6",
            approver_id="checker",
            approver_is_authorized=True,
            idempotency_key="approve-6",
        )
        self.assertEqual("APPROVAL_PENDING", result)
        self.assertEqual("APPROVAL_PENDING", service.state("p-6"))
        self.assertEqual([], execution.calls)
        self.assertEqual(
            [("APPROVAL_ERROR", "p-6", "checker", "DEPENDENCY_UNAVAILABLE")],
            audit.events,
        )

    def test_repeated_submit_key_creates_one_approval_request(self):
        service, approval, execution, _ = self.service()
        first = service.submit(
            "p-7", "12000", initiator_id="maker", idempotency_key="submit-7"
        )
        second = service.submit(
            "p-7", "12000", initiator_id="maker", idempotency_key="submit-7"
        )
        self.assertEqual(first, second)
        self.assertEqual(["p-7"], approval.requests)
        self.assertEqual([], execution.calls)

    def test_repeated_approval_key_creates_one_decision_and_execution(self):
        service, approval, execution, _ = self.service()
        service.submit(
            "p-8", "12000", initiator_id="maker", idempotency_key="submit-8"
        )
        first = service.approve(
            "p-8",
            approver_id="checker",
            approver_is_authorized=True,
            idempotency_key="approve-8",
        )
        second = service.approve(
            "p-8",
            approver_id="checker",
            approver_is_authorized=True,
            idempotency_key="approve-8",
        )
        self.assertEqual(first, second)
        self.assertEqual([("p-8", "checker")], approval.decisions)
        self.assertEqual(["p-8"], execution.calls)

    def test_invalid_amounts_cannot_fail_open(self):
        service, _, execution, _ = self.service()
        for index, amount in enumerate((None, "bad", "-0.01", 10000.0)):
            with self.subTest(amount=amount):
                with self.assertRaises(policy.InvalidAmount):
                    service.submit(
                        f"invalid-{index}",
                        amount,
                        initiator_id="maker",
                        idempotency_key=f"invalid-key-{index}",
                    )
        self.assertEqual([], execution.calls)

    def test_reused_idempotency_key_with_different_payload_is_rejected(self):
        service, _, execution, _ = self.service()
        service.submit(
            "p-9", "9999", initiator_id="maker", idempotency_key="submit-9"
        )
        with self.assertRaises(policy.IdempotencyConflict):
            service.submit(
                "p-10", "9999", initiator_id="maker", idempotency_key="submit-9"
            )
        self.assertEqual(["p-9"], execution.calls)


if __name__ == "__main__":
    unittest.main()
