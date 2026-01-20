from __future__ import annotations

import re
from typing import Literal


WhitespaceMode = Literal["collapse", "keep"]


def normalize_text(
    text: str,
    *,
    whitespace: WhitespaceMode = "collapse",
    strip: bool = True,
) -> str:
    """
    Basic normalization for problem / solution text.

    - Unifies common Unicode math symbols to ASCII (e.g. "−" -> "-", "×" -> "*").
    - Normalizes different quote types.
    - Normalizes whitespace (collapse multiple spaces, remove trailing spaces).
    """
    if text is None:
        return ""

    # Common Unicode → ASCII replacements
    replacements = {
        "\u2212": "-",  # minus sign
        "\u00d7": "*",  # multiplication sign
        "\u00b7": "*",  # middle dot
        "\u2217": "*",  # asterisk operator
        "\u00f7": "/",  # division sign
        "\u2264": "<=",  # ≤
        "\u2265": ">=",  # ≥
        "\u2260": "!=",  # ≠
        "\u2013": "-",  # en dash
        "\u2014": "-",  # em dash
        "\u2018": "'",  # left single quote
        "\u2019": "'",  # right single quote
        "\u201c": '"',  # left double quote
        "\u201d": '"',  # right double quote
    }

    for src, dst in replacements.items():
        text = text.replace(src, dst)

    # Normalize whitespace
    if whitespace == "collapse":
        # Collapse runs of whitespace to a single space, but keep newlines
        text = re.sub(r"[ \t]+", " ", text)
        # Remove spaces at line starts/ends
        text = "\n".join(line.strip() for line in text.splitlines())
    elif strip:
        text = text.strip()

    # Final global strip if requested
    if strip:
        text = text.strip()

    return text


def normalize_problem_and_solution(problem: str, solution: str) -> tuple[str, str]:
    """
    Convenience helper to normalize both problem and solution texts.
    """
    return normalize_text(problem), normalize_text(solution)

