"""
Evaluator Module

This module contains scoring functions used by the refactoring agent:
- Code readability score
- Cyclomatic complexity
- Linting / PEP8 compliance using flake8
"""

import subprocess
import ast


def flake8_score(code: str) -> int:
    """
    Returns the number of flake8 warnings.
    Lower is better.
    """
    with open("tmp_code.py", "w") as f:
        f.write(code)

    result = subprocess.run(
        ["flake8", "tmp_code.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    warnings = result.stdout.strip().split("\n")
    if warnings == ['']:
        return 0  # No warnings
    return len(warnings)


def cyclomatic_complexity(code: str) -> int:
    """
    Computes a VERY simple cyclomatic complexity:
    counts branching keywords.
    """
    tree = ast.parse(code)
    keywords = (ast.If, ast.For, ast.While, ast.Try, ast.With)

    count = 0
    for node in ast.walk(tree):
        if isinstance(node, keywords):
            count += 1
    return count


def readability_score(code: str) -> int:
    """
    Simple heuristic:
    - shorter lines = better
    - fewer nested blocks = better
    - more docstrings = better
    """
    lines = code.split("\n")
    avg_len = sum(len(l) for l in lines) / max(len(lines), 1)
    docstrings = code.count('"""')

    score = int(avg_len) - docstrings
    return max(score, 0)


def overall_score(code: str) -> float:
    """
    Combine scores into a single scalar.
    Lower score is better (fewer warnings, simpler, more readable).
    """
    f8 = flake8_score(code)
    cc = cyclomatic_complexity(code)
    rs = readability_score(code)

    return f8 + cc + rs
