# First coding-agent workflow: explain → fix → test → review
A working API connection is only the start. This small exercise shows how to give an agent a precise task, review its plan, and verify the result independently. Use after a plain chat test passes, with Hermes (setup-hermes), OpenCode (setup-opencode) or Aider (setup-aider). 9Router is a gateway between tool and AvalAI, not a coding agent. Checked 2026-09-08. **The exercise was executed offline for this skill: 5 tests, 3 fail before the fix, all 5 pass after a correct fix.**

## 1. Two practice files (fresh empty dir OUTSIDE any real repo; Python ≥3.10, no packages; no customer data/env files)
```python
# totals.py (intentionally incomplete)
def total_cents(prices):
    return sum(prices)
```
```python
# test_totals.py
import unittest
from totals import total_cents
class TotalsTests(unittest.TestCase):
    def test_empty(self): self.assertEqual(total_cents([]), 0)
    def test_integer_cents(self): self.assertEqual(total_cents([125, 250]), 375)
    def test_negative_rejected(self):
        with self.assertRaises(ValueError): total_cents([125, -1])
    def test_fraction_rejected(self):
        with self.assertRaises(ValueError): total_cents([1.5])
    def test_boolean_rejected(self):
        with self.assertRaises(ValueError): total_cents([True])
if __name__ == "__main__": unittest.main()
```
Contract: integer cents only, no negatives, no booleans, empty → 0, invalid → `ValueError`. (Teaching function, not accounting software.)

## 2. Baseline you run yourself
`python3 -m unittest -v test_totals.py` → expected **5 run, 3 fail** (negative/fraction/bool accepted). Don't let the agent weaken tests to get green.

## 3. Read-only plan
Prompt: "Read only totals.py and test_totals.py. Explain why the tests fail. Propose the smallest fix, but do not edit yet. Contract: … Do not install packages, read secrets, access the network, or change tests." Approve only reading those two files. Check the proposal handles `bool` being a subclass of `int` (e.g. `type(p) is int`, not `isinstance`) and keeps valid sums. Aider: `--chat-mode ask`, add these two files instead of README; OpenCode: keep approvals; Hermes: review enabled tool permissions. Text instructions alone aren't a sandbox.

## 4. One scoped edit
"Approved: edit only totals.py to satisfy that contract. Do not change test_totals.py or other files. Stop after the patch and report what changed. Do not commit, push, deploy, or claim tests ran unless you actually ran them." Aider: `/chat-mode code` for this step only, keep auto-commits off. Don't grant broad shell/network for a small fix.
Reference-correct fix (verified): loop; `if type(p) is not int or p < 0: raise ValueError(...)`; accumulate.

## 5. Verify independently
Re-run the same command → expected **all 5 pass**; confirm `test_totals.py` unchanged; in a Git repo also `git diff` + `git status --short`. Review report template: Scope / Behavior / Evidence (command) / Result (5 passed) / Unchanged / Not done (commit, push, deploy) — fill from commands YOU ran, don't copy agent claims. If a test still fails send only the needed error and ask for a revised plan; don't send unrelated env vars/private files.

## 6. Apply to real work
| who | first small task | acceptance evidence |
|---|---|---|
| developer | fix one validation bug | repro test, limited diff, related suite |
| startup | add one CSV import rule | synthetic valid+invalid rows, no customer data |
| student | explain a function, then attempt the fix yourself | your explanation + your own tests, within course rules |
| company team | read-only review of one module | file+line evidence, limits, human decision |
Before starting fix scope, tests, stop condition, permissions; cap request count/time per task; monitor AvalAI usage (agent loops/retries add cost; don't assume an SDK dollar-budget option works in every tool). For longer work keep a short note (current files, decisions, evidence, open questions); start a fresh session when context gets noisy; continuing an old session isn't independent verification — re-check on current files.

## Sources / limits
Adapted from OpenAI Cookbook (iterating development workflows with Codex) and Claude Cookbooks scheduled repository reviewer; keeps limited reads, explicit approval, evidence. Doesn't install Claude Agent SDK, run scheduled reviewers, or call hosted agent features AvalAI APIs.
