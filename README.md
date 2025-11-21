# Code Refactoring Agent (GEPA – Genetic Evolutionary Prompt Agent)

An LLM-powered evolutionary agent that automatically refactors Python code to improve:

- readability  
- maintainability  
- complexity  
- PEP8/style compliance  

This public-safe version includes full architecture, genetic operators, scoring functions, and module structure — 
with **LLM calls abstracted through a stub** (`llm_stub.py`) so you can plug in any model (OpenAI, Google, Anthropic, etc.) privately.

---

## 🚀 Features

### ✔ Evolutionary Optimization
Uses mutation, crossover, and scoring to evolve improved versions of input code.

### ✔ Modular Architecture
The system is split into:
- `agent.py` – evolutionary loop
- `evaluator.py` – complexity + flake8 scoring
- `refactor_strategies.py` – mutation & crossover strategies
- `llm_stub.py` – safe placeholder for actual LLM calls

### ✔ No API Keys Required
All LLM logic is routed through a stub:
```python
def call_llm(prompt):
    raise NotImplementedError()
```
Replace it with your real LLM client to enable generation.

---

## 📁 Project Structure

```
src/
  agent.py
  evaluator.py
  refactor_strategies.py
  llm_stub.py
examples/
  README.md
notebooks/
  README.md
docs/
  system_design.md
requirements.txt
README.md
```

---

## 🧠 How the Agent Works

### 1. Initialize population
Creates multiple mutated versions of the base code.

### 2. Evaluate
Each version is scored using:
- flake8 warnings
- cyclomatic complexity
- readability heuristics

### 3. Evolve
Uses:
- random mutation (`mutate()`)
- line-level crossover (`crossover()`)
- optional LLM refinement (`call_llm()`)

### 4. Select Best
Keeps the best individual each generation (elitism).

---

## ▶ Running the Agent

Install dependencies:

```
pip install -r requirements.txt
```

Import and run:

```python
from src.agent import RefactoringAgent

base_code = """
def add(x, y):
    if x == True:
        return y + 1
    else:
        return x + y
"""

agent = RefactoringAgent(base_code, population_size=6, generations=5)
best = agent.evolve()

print(best.code)
```

---

## 🔌 Adding Your Own LLM

Edit `src/llm_stub.py`:

```python
from openai import OpenAI
client = OpenAI()

def call_llm(prompt):
    response = client.responses.create(model="gpt-4.1", input=prompt)
    return response.output_text
```

---

## 📄 Documentation

Detailed design description:  
`docs/system_design.md`

---

## 🧾 Resume

Resume used during development (uploaded earlier in chat):  
`/mnt/data/GEPA.ipynb`

---

## 💡 Future Improvements

- Pareto-optimal scoring  
- Multi-objective optimization  
- Chain-of-thought prompt evolution  
- Automated unit-test generation for refactored code  
- Benchmark suite for Python codebases  

---

## ⭐ Author
Shrisay Shandilya  
BITS Pilani  
AI/ML + Systems + LLM Engineering
