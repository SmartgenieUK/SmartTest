import importlib
import os
import unittest


policy = importlib.import_module(
    os.environ.get("SMARTTEST_PAYMENT_MODULE", "payment_approval")
)


class StubGateway:
    def __init__(self, result=True, unavailable=False):
        self.result = result
        self.unavailable = unavailable
        self.calls = []

    def approve(self, payment_id):
        self.calls.append(payment_id)
        if self.unavailable:
            raise policy.ApprovalUnavailable("approval dependency unavailable")
        return self.result


class PaymentApprovalTests(unittest.TestCase):
    def test_below_threshold_does_not_call_approval_dependency(self):
        gateway = StubGateway()
        service = policy.PaymentApprovalService(gateway)

        self.assertEqual("APPROVED", service.decide("p-1", "9999.99"))
        self.assertEqual([], gateway.calls)

    def test_exact_threshold_requires_authorized_secondary_approval(self):
        gateway = StubGateway()
        service = policy.PaymentApprovalService(gateway)

        result = service.decide(
            "p-2", "10000.00", approver_is_authorized=True
        )

        self.assertEqual("APPROVED", result)
        self.assertEqual(["p-2"], gateway.calls)

    def test_above_threshold_requires_secondary_approval(self):
        gateway = StubGateway(result=False)
        service = policy.PaymentApprovalService(gateway)

        result = service.decide(
            "p-3", "10000.01", approver_is_authorized=True
        )

        self.assertEqual("REJECTED", result)
        self.assertEqual(["p-3"], gateway.calls)

    def test_unauthorized_approval_is_blocked_without_gateway_call(self):
        gateway = StubGateway()
        service = policy.PaymentApprovalService(gateway)

        self.assertEqual("BLOCKED_UNAUTHORIZED", service.decide("p-4", "12000"))
        self.assertEqual([], gateway.calls)

    def test_dependency_failure_leaves_payment_pending(self):
        gateway = StubGateway(unavailable=True)
        service = policy.PaymentApprovalService(gateway)

        result = service.decide(
            "p-5", "12000", approver_is_authorized=True
        )

        self.assertEqual("PENDING_APPROVAL", result)

    def test_duplicate_decision_is_rejected(self):
        gateway = StubGateway()
        service = policy.PaymentApprovalService(gateway)
        service.decide("p-6", "12000", approver_is_authorized=True)

        with self.assertRaises(policy.DuplicateDecision):
            service.decide("p-6", "12000", approver_is_authorized=True)


if __name__ == "__main__":
    unittest.main()
