# System Design – Code Refactoring Agent

This document describes the architecture, components, and workflow of the LLM-based code refactoring agent.

## Components
- **Refactoring Agent**: Receives input code, decides which refactoring strategies to apply.
- **Evaluator Module**: Scores readability, complexity, and best-practice compliance.
- **Refactoring Strategies**: Modular strategies applied based on evaluations.
- **LLM Backend**: Generates improved code using structured prompts and constraints.

## Workflow
1. User submits raw code.
2. Agent evaluates the code.
3. Agent selects the refactoring strategy.
4. LLM generates improved code.
5. Evaluator compares old vs new and validates improvement.

(More details will be added later.)
