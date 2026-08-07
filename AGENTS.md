# SmartTest Repository Agent Rules

1. Read relevant requirements and acceptance criteria before changing behaviour.
2. Inspect the authoritative existing tests before creating or relocating tests.
3. Explicitly address testing for every material change. If no executable test is appropriate, record why and identify alternative evidence.
4. Support behaviour-bearing changes with verification evidence; a passing pipeline is not sufficient when relevant checks are absent.
5. Consider happy paths, boundaries, invalid and failure paths, permissions, integrations, and regression according to risk.
6. Do not equate test count, code coverage, or tool status with correctness or requirement coverage.
7. Do not let implementation and AI-generated tests mutually validate the same interpretation when consequence warrants independent derivation or review.
8. For non-trivial defects, reproduce and establish causal evidence before claiming root cause; protect corrected behaviour with regression evidence.
9. Assess blast radius beyond edited files, including consumers, contracts, callbacks, persistence, security boundaries, and operations as applicable.
10. For production-affecting work, define healthy signals, failure signals, and rollback or remediation triggers.
11. Treat external tools as evidence providers, not substitutes for engineering judgement.
12. Report missing, unavailable, contradictory, or waived evidence honestly. Never turn an unexplained boolean into a release claim.
