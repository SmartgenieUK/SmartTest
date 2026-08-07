#!/usr/bin/env python3
"""Deterministic, standard-library verification for the SmartTest repository."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "LICENSE",
    "REPORT_CARD.md",
    "doctrine/TESTING_DOCTRINE.md",
    "docs/ADOPTION_GUIDE.md",
    "docs/AGENT_SETUP.md",
    "checklists/AI_CODE_RELEASE_CHECKLIST.md",
    "templates/TEST_PLAN_TEMPLATE.md",
    "templates/REQUIREMENT_TEST_TRACEABILITY_TEMPLATE.md",
    "templates/AI_CODE_DEFINITION_OF_DONE.md",
    "examples/payment-approval-python/test_payment_approval.py",
    "evidence/audits/ADOPTION_AUDIT.md",
    "evidence/audits/DOCTRINE_AUDIT.md",
)
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def github_slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value).strip().lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"\s+", "-", value)


def markdown_checks() -> list[str]:
    errors: list[str] = []
    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        if sum(1 for line in text.splitlines() if line.lstrip().startswith("```")) % 2:
            errors.append(f"unbalanced fenced code block: {path.relative_to(ROOT)}")

        anchors = {github_slug(match) for match in HEADING.findall(text)}
        for raw_target in LINK.findall(text):
            target = raw_target.strip().strip("<>").split(maxsplit=1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            file_part, separator, anchor = target.partition("#")
            linked = path if not file_part else (path.parent / unquote(file_part)).resolve()
            if not linked.exists():
                errors.append(
                    f"broken link: {path.relative_to(ROOT)} -> {raw_target}"
                )
                continue
            if separator and linked.suffix.lower() == ".md":
                linked_text = linked.read_text(encoding="utf-8")
                linked_anchors = {github_slug(match) for match in HEADING.findall(linked_text)}
                if unquote(anchor).lower() not in linked_anchors:
                    errors.append(
                        f"broken anchor: {path.relative_to(ROOT)} -> {raw_target}"
                    )

    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\nname:" not in text or "\ndescription:" not in text:
            errors.append(f"invalid skill frontmatter: {skill.relative_to(ROOT)}")
    return errors


def run_example(module: str) -> subprocess.CompletedProcess[str]:
    example = ROOT / "examples" / "payment-approval-python"
    environment = os.environ.copy()
    environment["SMARTTEST_PAYMENT_MODULE"] = module
    return subprocess.run(
        [sys.executable, "-m", "unittest", "-v", "test_payment_approval.py"],
        cwd=example,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    errors = [f"missing required file: {item}" for item in REQUIRED if not (ROOT / item).is_file()]
    errors.extend(markdown_checks())

    correct = run_example("payment_approval")
    correct_output = correct.stdout + correct.stderr
    if correct.returncode != 0 or "Ran 10 tests" not in correct_output or "OK" not in correct_output:
        errors.append("correct payment example did not pass all 10 tests")

    mutant = run_example("payment_approval_mutant")
    mutant_output = mutant.stdout + mutant.stderr
    expected_test = "test_exact_threshold_waits_for_distinct_authorized_approval"
    if (
        mutant.returncode == 0
        or "Ran 10 tests" not in mutant_output
        or "FAILED (failures=1)" not in mutant_output
        or expected_test not in mutant_output
    ):
        errors.append("mutant did not produce the one expected boundary failure")

    if errors:
        print("SmartTest verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    count = len(list(ROOT.rglob("*.md")))
    print("SmartTest verification: PASS")
    print(f"- {count} Markdown files checked for local links and fenced-code structure")
    print("- skill frontmatter checked")
    print("- correct payment example: 10/10 tests passed")
    print(f"- deliberate mutant: exactly 1/10 failed ({expected_test})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
