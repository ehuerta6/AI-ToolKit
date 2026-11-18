---
name: retro
description: Review completed AI-assisted engineering work to identify concrete improvements to skills, rules, context, tooling, and automated checks.
---

# Retro

Use completed work as evidence for improving the AI engineering environment.

A retro evaluates the workflow, not the person.

Do not turn one unusual failure into a permanent global rule without evidence that the rule would help future work.

## Process

### 1. Read the evidence

Review the relevant:

- conversation or agent session;
- issue or spec;
- commits and diff;
- verification results;
- review findings;
- failures and rework.

When evaluating reusable configuration, record the artifact and the real task where it was used, plus the observed result or friction. If it has not been used in a real task, say it remains untested; passing a validator is not usage evidence.

### 2. Identify friction

Look for concrete problems in:

#### Context

- information was hard to find;
- instructions were duplicated;
- source-of-truth conflicts occurred;
- important context was loaded too late;
- too much irrelevant context was always loaded.

#### Skills

- a repeatable workflow was performed manually;
- a skill produced ambiguous behavior;
- a skill duplicated another skill;
- completion criteria were too weak.

#### Rules

- an important judgment rule was missing;
- an existing rule caused unnecessary friction;
- a rule belongs in a project instead of globally.

#### Automated checks

- an error could have been caught deterministically;
- an existing check was not being run;
- CI, linting, typing, tests, or validation had a gap.

Prefer automation over prose rules for mechanical failures.

When a deterministic check is proposed for a repeated, evidenced failure, demonstrate when feasible that it catches the historical failure and accepts the correct case. Prefer fixing architecture, types, checks, or tests over adding redundant prose. Catalog changes still require the user's approval; a retro recommendation does not adopt itself.

#### Tools

- repeated expensive or unnecessary tool usage;
- missing access caused guesswork;
- a simpler tool would have produced better evidence.

#### Workflow

- unnecessary approvals;
- excessive context switching;
- poor task boundaries;
- weak handoffs;
- implementation began before decisions were ready.

### 3. Propose improvements

For each meaningful finding include:

- evidence;
- what went wrong;
- proposed change;
- where the change belongs;
- expected benefit;
- risk or tradeoff.

Possible destinations:

- project instructions;
- global rule;
- skill;
- agent;
- template;
- deterministic check;
- no change.

### 4. Classify the result

Use:

- `testing` for a new idea that needs evidence;
- `accepted` when the user explicitly adopts it;
- `rejected` when the user explicitly rejects it;
- `default` when the user explicitly promotes it to normal workflow;
- `replaced` when a newer approach supersedes it.

A retro recommendation is not automatically adopted.

### 5. Route reusable AI Toolkit candidates

After completing the retro, assess whether any finding belongs in the canonical AI Toolkit repository (`ehuerta6/AI-ToolKit`) or only in the project where the work happened.

A candidate belongs in AI Toolkit only when the retro has concrete evidence from actual work that reusable AI Toolkit configuration caused or materially contributed to the friction, and there is a plausible benefit beyond the source project. Project-specific product behavior, architecture, local conventions, and one-off mistakes stay in their project. Identify the reusable artifact or workflow when possible. Keep untested explanations or benefits clearly marked as hypotheses; do not present them as policy.

Before creating an issue, search the canonical repository for a relevant existing issue, including closed issues. Add new evidence to an existing issue when the scope matches instead of creating a duplicate. If one or more distinct candidates qualify and no matching issue covers them, create one focused issue in the canonical repository. Give it a concise description and one section per candidate with:

- source project and task;
- observed friction and concrete evidence;
- affected AI Toolkit artifact, if known;
- proposed change and expected benefit;
- tradeoffs or uncertainty;
- testing and adoption status.

Keep the issue concise. Preserve the full retro in its source project; do not copy it into AI Toolkit. Exclude secrets, private data, and unnecessary project details. State that the issue records a proposal and does not authorize implementation, adoption, or promotion from `testing`.

If no candidate meets the evidence and reuse threshold, say so in the retro and create no issue. Never create an empty or speculative issue because a retro completed. If GitHub access, repository identity, or issue creation is unavailable, prepare a concise issue draft and state what prevented creation. Creating an issue is only a proposal; it does not authorize changing or adopting AI Toolkit configuration.

## Rules

- Evidence before policy.
- Do not create permanent rules from stylistic preference alone.
- Mechanical problems should usually become deterministic checks.
- Avoid duplicating instructions across files.
- Keep always-loaded context small.
- Distinguish one-off mistakes from recurring workflow problems.
- The user decides whether a proposed change becomes part of the workflow.

## Completion

A retro is complete when it clearly states:

- what worked;
- what caused friction;
- what should change;
- where the change belongs;
- what should remain unchanged;
- which recommendations still require testing;
- whether any evidence-backed, reusable AI Toolkit candidate qualified for an issue, and whether that issue was created or an existing issue updated.
