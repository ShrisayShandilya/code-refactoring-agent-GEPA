"""
Refactoring Strategies Module

Contains mutation and crossover functions used by the evolutionary
refactoring agent. These operate on Python code strings or AST trees
and produce modified variants.
"""

import ast
import astunparse
import random


def mutate_variable_names(code: str) -> str:
    """
    Renames variable identifiers randomly.
    Helps improve naming consistency and readability.
    """

    class RenameVars(ast.NodeTransformer):
        def visit_Name(self, node):
            if random.random() < 0.2:  # 20% chance to rename
                node.id = node.id + "_v"
            return node

    tree = ast.parse(code)
    tree = RenameVars().visit(tree)
    return astunparse.unparse(tree)


def simplify_if_conditions(code: str) -> str:
    """
    Simplifies trivial if-conditions like:
    if x == True  ->  if x
    """
    tree = ast.parse(code)

    class Simplify(ast.NodeTransformer):
        def visit_Compare(self, node):
            # Replace x == True → x
            if (
                isinstance(node.left, ast.Name)
                and len(node.comparators) == 1
                and isinstance(node.comparators[0], ast.Constant)
                and node.comparators[0].value is True
            ):
                return node.left
            return node

    tree = Simplify().visit(tree)
    return astunparse.unparse(tree)


def crossover(parent_a: str, parent_b: str) -> str:
    """
    Combines lines from two parent programs.
    """
    a_lines = parent_a.split("\n")
    b_lines = parent_b.split("\n")

    split_a = random.randint(0, len(a_lines))
    split_b = random.randint(0, len(b_lines))

    new_code = "\n".join(a_lines[:split_a] + b_lines[split_b:])
    return new_code


def mutate(code: str) -> str:
    """
    Apply a random mutation strategy.
    """
    strategies = [mutate_variable_names, simplify_if_conditions]
    strategy = random.choice(strategies)
    return strategy(code)
