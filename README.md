# Orydex — Summer Internship Training Program

Welcome aboard! 🎉

A warm welcome to **every trainee joining Orydex for the summer internship**. You
are here because we believe in your potential — now it is your turn to prove it to
yourself. Over the next several weeks you will sharpen your fundamentals, learn how
real engineering teams build and ship software, and then put it all together by
building something of your own.


You will get stuck. You will hit confusing errors. That is exactly where the
learning happens — push through it, ask good questions, and help the people next to
you. Be curious, be consistent, and treat every task as practice for the real
project at the end. Let's build something you'll be proud of.

## Internship at a Glance

The internship runs for about **1.5 months**, in three phases:

| Phase | When | What happens |
| --- | --- | --- |
| **1 — Learn** | First ~2.5 weeks | Work through the structured training tasks below to build core skills. |
| **2 — Build** | Middle weeks | You are assigned a **project** to design, build, and submit. |
| **3 — Demo & Feedback** | Final few days | You **demonstrate what you built**, followed by an **open feedback session**. |

Treat the learning phase as ramp-up for the project phase: the habits you form now
(clean code, small commits, tests, good PRs) are exactly what the project expects.

## Training Agenda

The program is a sequence of tasks. Complete them in order — each builds on the one
before it.

| Task | Topic | Status |
| --- | --- | --- |
| [Task 1](task1/README.md) | Python standards revision | ✅ Available |
| [Task 2](task2/README.md) | Git & GitHub workflow | ✅ Available |
| [Task 3](task3/README.md) | FastAPI — building web APIs | ✅ Available |
| [Task 4](task4/README.md) | Containerizing with Docker & Compose | ✅ Available |
| Task 5+ | Machine Learning | 🔜 Coming soon |
| Task 5+ | MCP (Model Context Protocol) | 🔜 Coming soon |
| Task 5+ | Kaggle / competitions | 🔜 Coming soon |
| Final | **Final Project** | 🔜 Coming soon |

> More tasks will be added during the program. If you forked this repository, sync
> the upstream changes to pull in new tasks (see below).

Each task folder has its own `README.md` with goals, learning resources, and a
submission checklist. **Start with [Task 1](task1/README.md).**

## Getting Started

### 1. Set up SSH access to GitHub

You will push over SSH. The full walkthrough (generate a key, add it to GitHub,
verify) is in **[Task 2](task2/README.md)** — do that first if you have not already.

### 2. Get your own copy of this repository

This repo is the source of truth for the program. Work in **your own copy** under
your GitHub account. (The exact repository URL is shared in the channel — replace
`orydex/summer-training` below if it differs.)

**Recommended — Fork** (lets you pull in new tasks later):

1. Click **Fork** at the top of this repository on GitHub.
2. Clone your fork:

   ```bash
   git clone git@github.com:<your-username>/summer-training.git
   cd summer-training
   ```

3. Track the original so you can sync new tasks:

   ```bash
   git remote add upstream https://github.com/TeamOrydex/summer-training.git
   # later, to pull in newly added tasks:
   git fetch upstream
   git switch main
   git merge upstream/main
   git push origin main
   ```

**Alternative — Clone and push to a new repo:** clone this repo, create an empty
repository on your GitHub account, then repoint `origin` to it:

```bash
git clone git@github.com:orydex/summer-training.git
cd summer-training
git remote set-url origin git@github.com:<your-username>/summer-training.git
git push -u origin main
```

### 3. Work through a task

```bash
git switch -c task1/python-standards-revision   # branch for the task
# ...do the work...
git add . && git commit -m "Meaningful message"
git push -u origin task1/python-standards-revision
# then open a pull request into main (see Branch Rules below)
```

## Branch Rules

These apply to **every task**:

1. **Never commit directly to `main`.** `main` always stays working.
2. **One branch per task,** created from an up-to-date `main`.
3. **Name the branch with the task prefix** — `task1/...`, `task2/...`, `task3/...`,
   `task4/...`. This matters: CI is wired to run on the matching prefix (e.g. the
   Task 1 and Task 3 checks only run on `task1/*` and `task3/*` branches).
4. **Commit small and often** with clear messages.
5. **Open a pull request into `main`** when the task is ready — do not merge your own
   work without review.
6. **Merge only after** the review is approved **and** CI is green.
7. Keep your branch up to date with `git fetch` + `git rebase origin/main`.

**Branch naming examples**

```text
task1/python-standards-revision
task2/github-workflow
task3/patient-api
task4/dockerize-api
fix/readme-typo
docs/update-task3
```

## Code Review & Reviewers

- Every change reaches `main` through a **pull request**.
- This repository is **public**, so you can add **as many reviewers as you like** to
  your PRs — do it.
- You will get the **list of reviewers from the channel.** Add the relevant mentors
  and peers to each PR you open.
- Reviewing others is part of the job: leave at least one helpful comment on a
  teammate's PR when you can.

## Submission Rules

1. All task work is submitted through pull requests in your copy of this repository.
2. Final submissions for code tasks must be runnable `.py` files (or the task's
   project structure) — not just notebooks.
3. Every task must have a clear `README.md` or follow the task's instructions.
4. Use meaningful file names — not generic ones like `problem1.py`.
5. **Never commit secrets** — passwords, API keys, tokens, private data, or **real
   patient data**. Use fake/sample data only.
6. Keep commits small and meaningful.
7. One branch per task; open a pull request for review before merging.

## Pull Request Expectations

Each pull request should explain:

- **What** was completed
- **Which files** changed
- **How to run / test** the code
- Any **known limitations** or open questions
- Screenshots or terminal output if useful

## General Code Expectations

- Code should run without manual editing.
- File and function names should be clear and descriptive.
- Avoid unnecessary code; comment only where it aids understanding.
- Follow standard Python style (PEP 8); pass the task's linter/tests where provided.

## Repository Structure

```text
summer-training/
├── README.md                     # you are here
├── .github/workflows/            # CI: runs tests/style per task branch
├── task1/                        # Python standards revision
│   ├── README.md
│   ├── p1_..p9_*.py              # the nine problems
│   ├── tests/                    # automated checks
│   ├── requirements.txt
│   └── ruff.toml
├── task2/
│   └── README.md                 # Git & GitHub workflow
├── task3/                        # FastAPI — Patient Management API
│   ├── README.md
│   ├── app/                      # the API you build
│   ├── tests/                    # your test suite (>98% coverage)
│   └── requirements.txt
└── task4/
    └── README.md                 # Dockerize the Task 3 API
```

Questions? Ask in the channel — early and often. Good luck, and welcome to Orydex. 🚀
