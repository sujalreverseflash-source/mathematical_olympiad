from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional


class CheckKind(Enum):
    FINAL_ANSWER = auto()
    STEP_ALGEBRA = auto()
    CONSTRAINT = auto()
    NUMERIC = auto()
    CODE = auto()


class CheckStatus(Enum):
    PASS_ = auto()
    FAIL = auto()
    UNKNOWN = auto()


@dataclass
class CheckResult:
    kind: CheckKind
    status: CheckStatus
    message: str = ""


@dataclass
class VerificationRequest:
    problem_text: str
    solution_text: str
    # optional reference / metadata can be added later
    reference_answer: Optional[str] = None


@dataclass
class VerificationResult:
    is_consistent: bool
    score: float
    final_answer_ok: bool
    check_results: List[CheckResult]
    trace: str = ""

