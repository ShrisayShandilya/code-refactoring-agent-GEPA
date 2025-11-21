"""
GEPA – Genetic Evolutionary Prompt Agent (Safe Public Version)

This module implements the core evolutionary algorithm used to
refactor code using:
- mutation
- crossover
- LLM-based improvements (via stub)
- evaluation scoring

LLM access is abstracted in llm_stub.call_llm() so this repo remains public-safe.
"""

import random
from typing import List
from .refactor_strategies import mutate, crossover
from .evaluator import overall_score
from .llm_stub import call_llm


class Individual:
    """Represents a candidate program in the population."""

    def __init__(self, code: str):
        self.code = code
        self.score = None

    def evaluate(self):
        """Compute fitness score."""
        self.score = overall_score(self.code)
        return self.score


class RefactoringAgent:
    """
    Main evolutionary refactoring agent.

    Steps:
    1. Initialize population
    2. Evaluate all individuals
    3. Mutate + crossover
    4. Use LLM-based refinement (optional)
    5. Select best individuals
    """

    def __init__(
        self,
        base_code: str,
        population_size: int = 6,
        generations: int = 5,
        llm_enabled: bool = False
    ):
        self.base_code = base_code
        self.population_size = population_size
        self.generations = generations
        self.llm_enabled = llm_enabled

    def initialize_population(self) -> List[Individual]:
        population = []

        # Base individual (unmodified)
        population.append(Individual(self.base_code))

        # Mutated initial variants
        for _ in range(self.population_size - 1):
            mutated = mutate(self.base_code)
            population.append(Individual(mutated))

        return population

    def llm_refine(self, code: str) -> str:
        """
        Calls the LLM stub for rewriting code.
        Replace stub implementation in llm_stub.py to enable.
        """
        try:
            prompt = f"Refactor the following Python code:\n\n{code}\n\nReturn only the improved code."
            return call_llm(prompt)
        except NotImplementedError:
            return code  # Safe fallback if LLM unavailable

    def evolve(self) -> Individual:
        """Run the evolutionary loop."""

        population = self.initialize_population()

        for gen in range(self.generations):
            print(f"\nGeneration {gen+1}/{self.generations}")

            # Evaluate
            for ind in population:
                ind.evaluate()

            # Sort by score (lower is better)
            population.sort(key=lambda x: x.score)
            best = population[0]
            print(f"  Best score: {best.score}")

            # Produce offspring
            new_population = [best]  # elitism

            while len(new_population) < self.population_size:
                parent_a = random.choice(population[:3])
                parent_b = random.choice(population[:3])

                child_code = crossover(parent_a.code, parent_b.code)
                child_code = mutate(child_code)

                # Optional LLM step
                if self.llm_enabled:
                    child_code = self.llm_refine(child_code)

                new_population.append(Individual(child_code))

            population = new_population

        # Final evaluation
        for ind in population:
            ind.evaluate()

        population.sort(key=lambda x: x.score)
        return population[0]
