---
name: project-audit
description: Audit a project's AI configuration against current project needs and AI Toolkit to detect duplication, drift, stale instructions, and missing reusable configuration.
---

# Project audit

Audit an existing project's AI configuration.

## Inspect

Read:

- project instructions and AGENTS files;
- current skills, agents, rules, and templates;
- product and architecture sources;
- Git workflow;
- the canonical AI Toolkit `README.md`;
- the canonical AI Toolkit `WORKFLOWS.md`.

Use an accessible checkout or supplied copies when available. If the toolkit
catalog or workflow guide is unavailable, continue with the target project's
configuration and report that comparison as incomplete; do not infer missing
catalog guidance or block the audit on an inaccessible checkout.

## Classify

For each relevant configuration item return:

- KEEP — correct and project-specific;
- UPDATE — still useful but stale or weaker;
- REMOVE — unnecessary or duplicated;
- MOVE — reusable behavior that belongs in AI Toolkit;
- ADD — useful configuration currently missing.

## Check for

- duplicated instructions;
- conflicting sources of truth;
- stale project decisions;
- copied skills that drifted from canonical versions;
- oversized instruction files;
- configuration with no evidence of use;
- recurring friction or successful outcomes recorded in retros or task history;
- generic rules embedded in project-specific context.

Treat missing usage evidence as unknown, not proof that configuration is unused. Do not infer adoption or acceptance from catalog presence; rely on explicit decisions and usage evidence.

Project-specific behavior wins over reusable defaults.

Do not make changes until the proposed cleanup is approved.

## Completion

Return:

- findings;
- recommended changes;
- affected files;
- migration risks.
