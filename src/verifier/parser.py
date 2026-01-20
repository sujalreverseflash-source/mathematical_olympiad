from __future__ import annotations

import re
from typing import List, Optional

from .normalization import normalize_text


LATEX_INLINE_MATH = re.compile(r"\$(.+?)\$")
LATEX_DISPLAY_MATH = re.compile(r"\\\[(.+?)\\\]")


def extract_latex_math_blocks(text: str) -> List[str]:
    """
    Extract LaTeX math segments like $...$ and \[ ... \].

    This is a very rough first step; later we can make this smarter
    and feed the extracted strings into SymPy / latex2sympy.
    """
    blocks: List[str] = []
    blocks.extend(match.group(1) for match in LATEX_INLINE_MATH.finditer(text))
    blocks.extend(match.group(1) for match in LATEX_DISPLAY_MATH.finditer(text))
    return blocks


def extract_final_answer(solution_text: str) -> Optional[str]:
    """
    Heuristic: take the *last* LaTeX math block as the final answer.

    In many AIMO-style solutions, the final numeric/expression answer
    is written in math mode at the end. We will refine this later.
    """
    norm = normalize_text(solution_text)
    blocks = extract_latex_math_blocks(norm)
    if not blocks:
        return None
    return blocks[-1].strip()


def extract_intermediate_equations(solution_text: str) -> List[str]:
    """
    Return all math blocks except (heuristically) the final one,
    to be treated as intermediate steps.
    """
    norm = normalize_text(solution_text)
    blocks = extract_latex_math_blocks(norm)
    if len(blocks) <= 1:
        return []
    return [b.strip() for b in blocks[:-1]]

