# Task 2 — Git & GitHub Workflow

## Purpose

This task is focused on professional Git and GitHub workflow.

As a trainee, you already wrote the Task 1 code. Now you will learn how software
teams actually ship that code: connecting to GitHub over SSH, working on a
branch, making clean commits, keeping the branch up to date, and opening a pull
request (PR) for review.

**Your deliverable for Task 2 is to open the pull request for your Task 1 work.**
Everything below builds the Git understanding you need to do that well.

## AI Usage Rule

AI tools are allowed for this task, but only in a controlled way.

You **may** use AI to explain Git errors, improve a pull request description,
review commit-message clarity, summarize changes, and suggest debugging steps.

You **may not** use AI to create fake commits or pull requests, generate false
evidence, bypass code review, or blindly copy commands you do not understand.

## What You Will Practice

By the end of this task you should understand and be able to use:

- **SSH authentication** — connecting to GitHub securely without a password
- **`clone`** — copying a remote repository to your machine
- **`remote`** — the named link between your local repo and GitHub
- **`fetch`** — downloading remote changes without touching your files
- **`pull`** — `fetch` + merge into your current branch
- **`push`** — uploading your commits to the remote
- **`branch`** — isolating your work from `main`
- **`commit`** — recording a small, meaningful unit of change
- **`rebase`** — replaying your commits on top of the latest `main`
- **`squash`** — combining several commits into one before review

## Git Command Reference

| Command | What it does |
| --- | --- |
| `git clone <url>` | Copy a remote repository (and its history) to your machine |
| `git remote -v` | Show the remotes your repo is connected to |
| `git fetch origin` | Download new commits/branches from the remote — your files do **not** change |
| `git pull` | `git fetch` **and** merge the remote branch into your current branch |
| `git push -u origin <branch>` | Upload your branch and set it to track the remote |
| `git branch` / `git switch -c <name>` | List branches / create and switch to a new branch |
| `git add <files>` + `git commit -m "..."` | Stage changes, then record them as a commit |
| `git status` / `git log --oneline` | See what changed / view commit history |
| `git rebase origin/main` | Replay your commits on top of the latest `main` (linear history) |
| `git rebase -i <base>` | Interactively reorder, edit, or **squash** commits before sharing |

> Rule of thumb: **`fetch` is safe** (it only downloads). **`pull`, `rebase`, and
> `push` change history or files** — read what they print.

## Learning Resources

**Start here**

- [Pro Git book](https://git-scm.com/book/en/v2) — free, official, and thorough. Chapters 2–3 cover everything in this task.
- [Learn Git Branching](https://learngitbranching.js.org/) — interactive, visual practice for branch/merge/rebase.

**Watch (short refreshers)**

- [Git Explained in 100 Seconds](https://www.youtube.com/watch?v=hwP7WQkmECE) — Fireship; the whole mental model (repo, commit, branch, merge) in under two minutes.
- [Git & GitHub Crash Course for Beginners](https://www.youtube.com/watch?v=SWYqp7iY_Tc) — Traversy Media; clone, branch, commit, push, and pull requests in ~30 minutes.

**By topic**

| Topic | Resource |
| --- | --- |
| SSH keys for GitHub | [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) |
| Clone / remote / fetch / pull / push | [Atlassian: Syncing](https://www.atlassian.com/git/tutorials/syncing) |
| Branches | [Atlassian: Using branches](https://www.atlassian.com/git/tutorials/using-branches) |
| Writing good commits | [How to write a Git commit message](https://cbea.ms/git-commit/) |
| Rebase & squash | [`git rebase` docs](https://git-scm.com/docs/git-rebase) · [Atlassian: Rewriting history](https://www.atlassian.com/git/tutorials/rewriting-history) |
| Pull requests | [GitHub: About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) |

**More practice**

- [GitHub Skills](https://skills.github.com/) — short, hands-on GitHub courses.
- [Oh My Git!](https://ohmygit.org/) — a game for learning Git.

## The Task — Open the Pull Request for Task 1

Your goal is to get your Task 1 work onto a branch and open a PR into `main`.
Use a branch named `task1/...` so the Task 1 CI (`ruff` + `pytest`) runs on your
pull request.

```text
Suggested branch name: task1/python-standards-revision
```

### Step 0 — Configure your Git identity

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Step 1 — Set up SSH access to GitHub

Create a key (skip if you already have `~/.ssh/id_ed25519`):

```bash
ssh-keygen -t ed25519 -C "you@example.com"   # press Enter to accept defaults
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Copy the **public** key and add it to GitHub under
**Settings → SSH and GPG keys → New SSH key**:

```bash
cat ~/.ssh/id_ed25519.pub
```

Verify the connection:

```bash
ssh -T git@github.com   # expect a "successfully authenticated" message
```

### Step 2 — Connect your repo to GitHub over SSH

Check whether a remote already exists:

```bash
git remote -v
```

- If `origin` is listed with an `https://` URL, switch it to SSH:

  ```bash
  git remote set-url origin git@github.com:<org-or-user>/<repo>.git
  ```

- If there is **no** remote yet, add one (create the empty repo on GitHub first):

  ```bash
  git remote add origin git@github.com:<org-or-user>/<repo>.git
  ```

> For reference, a teammate starting fresh would copy the repo with
> `git clone git@github.com:<org-or-user>/<repo>.git`.

### Step 3 — Create the Task 1 branch

```bash
git switch main      # or: git switch master
git pull             # make sure main is up to date
git checkout -b task1/python-standards-revision
```

### Step 4 — Commit Task 1 in small, meaningful steps

Aim for several focused commits rather than one giant commit. For example:

```bash
git add task1/p1_patient_summary.py task1/p2_collection_operations.py
git commit -m "Add patient summary and collection operations"

git add task1/p3_dictionary_analysis.py task1/p4_slicing_and_loops.py
git commit -m "Add dictionary analysis and slicing/loops"

git add task1/p5_functions_and_lambdas.py task1/p6_triage_report.py
git commit -m "Add functions/lambdas and triage report"

git add task1/p7_runner_up.py task1/p8_minion_game.py task1/p9_word_order.py
git commit -m "Add HackerRank practice problems (p7-p9)"
```

Check your work as you go:

```bash
git status
git log --oneline
```

### Step 5 — Push your branch

```bash
git push -u origin task1/python-standards-revision
```

### Step 6 — Keep your branch up to date

If `main` moved on while you worked, bring your branch up to date with a rebase
(replays your commits on top of the latest `main`):

```bash
git fetch origin
git rebase origin/main
# resolve any conflicts, then:
git push --force-with-lease
```

### Step 7 — Tidy your history with a squash (optional but encouraged)

If you made messy "fix typo" commits, squash them into clean ones before review:

```bash
git rebase -i origin/main
```

In the editor, keep the first commit as `pick` and change later ones to `squash`
(or `s`). Save to combine them, then `git push --force-with-lease`.

> `--force-with-lease` is the safe way to overwrite a pushed branch: it refuses
> the push if someone else has pushed in the meantime.

### Step 8 — Open the pull request

On GitHub, open a PR from `task1/python-standards-revision` into `main` with the
title:

```text
Task 1: Python standards revision
```

Use this description template:

```markdown
## Summary
What this PR adds (the Task 1 solutions).

## Changes Made
- Implemented problems p1–p9
- (anything else)

## How to Review
Which files to look at, and how to run the tests:
`pip install -r task1/requirements.txt && pytest task1/tests`

## Notes
Anything incomplete, or questions for the reviewer.
```

### Step 9 — Pass CI, respond to review, then merge

- Make sure the **Task 1 Tests** check (ruff + pytest) is green.
- Address review comments with new commits (or a follow-up rebase).
- Merge into `main` only after approval and a green build.

## Reflection

Add your reflection here before submitting:

```text
1. The most useful Git command I used was:
2. One Git mistake or confusion I faced was:
3. What is the difference between `fetch` and `pull`?
4. When would you rebase instead of merge?
5. Pull requests are useful because:
```

## Submission Checklist

- [ ] I set up SSH access to GitHub and verified it with `ssh -T git@github.com`.
- [ ] My repo's `origin` remote uses the SSH URL.
- [ ] I created a `task1/...` branch for the Task 1 work.
- [ ] I made several small, meaningful commits (not one giant commit).
- [ ] I kept my branch up to date with `git fetch` + `git rebase`.
- [ ] I opened a pull request into `main` with a clear description.
- [ ] The **Task 1 Tests** CI check is green.
- [ ] I did not commit secrets or real patient data.
- [ ] My final `git status` is clean.
