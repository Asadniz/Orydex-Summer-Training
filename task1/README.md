# Task 1 — Python Standards Revision

## Purpose

This task is a Python revision exercise. It is not a beginner-level Python course.

As a trainee, you have already studied programming concepts during your bachelor's degree. This task helps you revise Python syntax, refresh important programming patterns, and identify any gaps before moving into GitHub workflows, APIs, Django/FastAPI, ML, Kaggle, Grand Challenge, and project work.

## AI Usage Rule

AI tools are prohibited for this task.

Do not use ChatGPT, Claude, Cursor, Copilot, or any other AI tool to solve these exercises.

AI will be allowed from the next task onward, but this first task must be completed independently so you can revise and demonstrate your own understanding of Python fundamentals.

## Getting Started

There is no notebook for this task — complete your work directly in the `.py`
files listed below.

Set up your environment once from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows PowerShell
pip install -r task1/requirements.txt
```

If you need to revise a topic, use the **Learning Resources** section below.

## What You Will Practice

- Python operations
- Lists, tuples, and sets
- Dictionaries and nested dictionaries
- Loops and inline loops
- List/set/dictionary comprehensions
- Slicing
- Functions
- Lambda functions
- Type hints
- Docstrings
- Basic error handling
- File handling
- Clean code structure
- Simple assertions for testing

## Learning Resources

You are expected to revise independently. Start with the official Python
tutorial, then use the topic links to fill specific gaps.

**Start here**

- [The Python Tutorial](https://docs.python.org/3/tutorial/) — the official, beginner-to-intermediate walkthrough.

**Watch (short refreshers)**

- [Python in 100 Seconds](https://www.youtube.com/watch?v=x7X9w_GIm1s) — Fireship; a 2-minute reminder of what Python is and why it looks the way it does.
- [Python for Beginners — Learn Python in 1 Hour](https://www.youtube.com/watch?v=kqtD5dpn9C8) — Programming with Mosh; a fast, complete pass over the fundamentals this task revises.

**By topic**

| Topic | Resource |
| --- | --- |
| Operations, variables, types | [An informal introduction to Python](https://docs.python.org/3/tutorial/introduction.html) |
| Lists, tuples, sets, dicts, comprehensions | [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) |
| Slicing | [Strings & slicing](https://docs.python.org/3/tutorial/introduction.html#strings) |
| Loops, `range`, `enumerate`, `zip` | [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) |
| Functions & lambda | [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) · [Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) |
| Error handling | [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) |
| File handling | [Input and Output](https://docs.python.org/3/tutorial/inputoutput.html) · [`pathlib`](https://docs.python.org/3/library/pathlib.html) · [`csv`](https://docs.python.org/3/library/csv.html) · [`json`](https://docs.python.org/3/library/json.html) |
| Counting & grouping | [`collections`](https://docs.python.org/3/library/collections.html) (e.g. `Counter`) |
| Type hints | [`typing`](https://docs.python.org/3/library/typing.html) · [PEP 484](https://peps.python.org/pep-0484/) |
| Dataclasses | [`dataclasses`](https://docs.python.org/3/library/dataclasses.html) |

**Standards & tooling**

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)
- [Ruff documentation](https://docs.astral.sh/ruff/) — the linter/formatter used in this task.
- [pytest documentation](https://docs.pytest.org/) — the test runner used in this task.

**More practice**

- [HackerRank — Python track](https://www.hackerrank.com/domains/python) — source of problems 7–9.
- [Real Python tutorials](https://realpython.com/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — free online book.

## Required Files

Complete the following files:

```text
task1/
├── p1_patient_summary.py
├── p2_collection_operations.py
├── p3_dictionary_analysis.py
├── p4_slicing_and_loops.py
├── p5_functions_and_lambdas.py
├── p6_triage_report.py
├── p7_runner_up.py
├── p8_minion_game.py
├── p9_word_order.py
├── requirements.txt
├── ruff.toml
└── tests/
    ├── conftest.py
    ├── test_p1_patient_summary.py
    ├── test_p2_collection_operations.py
    ├── test_p3_dictionary_analysis.py
    ├── test_p4_slicing_and_loops.py
    ├── test_p5_functions_and_lambdas.py
    ├── test_p6_triage_report.py
    ├── test_p7_runner_up.py
    ├── test_p8_minion_game.py
    └── test_p9_word_order.py
```

Files are prefixed `p1_`–`p9_` so they match the problem numbers below and
are easy to work through in order. Problems 1–6 are revision exercises;
problems 7–9 are practice problems from HackerRank.

## Problem 1 — `p1_patient_summary.py`

Create a script that stores fake patient records and calculates basic summary information.

Your script should include:

- a list of patient dictionaries,
- total number of patients,
- average age,
- number of active patients,
- list of unique conditions,
- count of patients by condition.

Expected concepts: lists, dictionaries, loops, basic operations, simple functions.

## Problem 2 — `p2_collection_operations.py`

Practice list, tuple, and set operations.

Your script should include examples of adding, removing, sorting, converting to a set, finding unique values, finding common values, and finding differences between sets.

Expected concepts: list methods, set operations, membership checks, clean variable naming.

## Problem 3 — `p3_dictionary_analysis.py`

Create nested dictionaries representing fake patient profiles.

Your script should include accessing nested values, updating values, safely reading missing keys using `.get()`, counting values from a list of dictionaries, and creating a summary dictionary.

Expected concepts: dictionaries, nested data, loops, `.get()`, key/value iteration.

## Problem 4 — `p4_slicing_and_loops.py`

Practice slicing and loop patterns.

Your script should include list slicing, string slicing, reversing a list, extracting first/last items, `range`, `enumerate`, `zip`, and list comprehensions.

Expected concepts: slicing, loops, inline loops, readable iteration.

## Problem 5 — `p5_functions_and_lambdas.py`

Create reusable functions for simple healthcare-style calculations.

Your script should include functions for calculating BMI, classifying BMI, converting names to title case, filtering active patients, and sorting patients using a lambda function.

Expected concepts: functions, parameters, return values, type hints, lambda functions.

## Problem 6 — `p6_triage_report.py`

Build a small triage report using fake patient records.

Your script should assign risk labels based on risk score, count patients by risk label, identify active high-risk patients, create a final report dictionary, and print the report clearly.

Expected concepts: functions, dictionaries, lists, loops, comprehensions, conditionals, basic testing with `assert`.

## HackerRank Practice Problems

Problems 7–9 are classic problems from the HackerRank Python track. Each one is
adapted into a single function so it can be checked by the tests. Implement the
function in the file; read the linked problem for the full description.

## Problem 7 — `p7_runner_up.py` (Easy)

[Find the Runner-Up Score!](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)

Given a list of scores, return the runner-up score — the second highest
*distinct* value.

Expected concepts: lists, sets, sorting.

## Problem 8 — `p8_minion_game.py` (Medium)

[The Minion Game](https://www.hackerrank.com/challenges/the-minion-game/problem)

Score substrings for two players (Kevin for vowel-started substrings, Stuart for
consonant-started ones) and return the winner and their score, or `"Draw"`.

Expected concepts: strings, loops, counting, conditionals.

## Problem 9 — `p9_word_order.py` (Medium)

[Word Order](https://www.hackerrank.com/challenges/word-order/problem)

Return the number of distinct words and how many times each appears, with the
counts ordered by each word's first appearance.

Expected concepts: dictionaries, ordering, counting.

## Check Your Understanding

Once you have finished, make sure you can answer these:

1. What is the difference between a list and a set?
2. Why use `.get()` when reading from a dictionary?
3. When should you use a comprehension instead of a loop?
4. What is the difference between `==` and `is`?
5. Why should functions return values instead of only printing?
6. When is a lambda useful, and when should you avoid it?
7. Why should you never use real patient data in training code?

## Submission Checklist

- [x] I completed all required `.py` files.
- [ ] I did not use AI for this task.
- [ ] I used fake/sample data only.
- [ ] My code runs without manual edits.
- [ ] I used meaningful variable and function names.
- [ ] I added simple tests or assertions where required.
- [ ] The style check passes (`ruff check task1`).
- [ ] The tests pass (`pytest task1/tests`).
- [ ] My pull request explains what I completed.

## How to Run

From the root of the repository:

```bash
python task1/p1_patient_summary.py
python task1/p2_collection_operations.py
python task1/p3_dictionary_analysis.py
python task1/p4_slicing_and_loops.py
python task1/p5_functions_and_lambdas.py
python task1/p6_triage_report.py
python task1/p7_runner_up.py
python task1/p8_minion_game.py
python task1/p9_word_order.py
```

## Running the Tests

Each problem has an automated test file in `task1/tests/`. Install the test
dependency once, then run the whole suite from the repository root:

```bash
pip install -r task1/requirements.txt
pytest task1/tests -v
```

The tests fail until you complete the functions — that is expected. Keep
implementing until every test passes. The tests describe the behaviour each
function must have, so read them if you are unsure what a function should do.

## Code Style

We use [ruff](https://docs.astral.sh/ruff/) for a light style check. The rules
are intentionally lenient — they cover formatting, import order, docstrings, and
common PEP 8 / likely-bug issues, and skip the pedantic ones. The config lives in
`task1/ruff.toml`.

```bash
ruff check task1          # report style issues
ruff check task1 --fix    # auto-fix what it safely can
ruff format task1         # auto-format the code
```

Tip: running `ruff check task1 --fix` and `ruff format task1` fixes most issues
for you.

## Continuous Integration

When you open a pull request from a branch named `task1/...`, GitHub Actions
runs the style check (`ruff`) and the tests (`pytest task1/tests`) automatically
(see `.github/workflows/task1-tests.yml`). Your PR is ready for review once the
**Task 1 Tests** check is green.

## Pull Request Title

```text
Task 1: Python standards revision
```
