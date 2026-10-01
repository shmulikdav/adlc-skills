# adlc-build — Execution stack & delivery shape

**ADLC phase:** 3 · Build

## Overview

Agentic construction at the system level: choosing and composing execution frameworks (Superpowers, Spec Kit, GSD, BMAD, built-in plan mode) with one owner per slot, small-batch delivery policy, and legacy modernization strategy with behavior parity.

## Install

```
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-build@adlc-skills
```

## Skills (3)

- `execution-rail-selection` — Use when choosing or combining agentic coding frameworks such as Superpowers, GSD, Spec Kit, BMAD, gstack, or Claude Code's built-in plan mode, when two installed frameworks conflict, or when a team asks which workflow plugin to standardize on
- `legacy-modernization` — Use when planning a rebuild, rewrite, framework or language migration of a legacy system with coding agents, auditing a legacy codebase before a rewrite, or deciding between strangler-fig migration and a full rewrite
- `small-batch-delivery` — Use when agent-generated pull requests are too large to review, review time is ballooning, a team asks how to keep AI-assisted delivery stable, or when writing PR policies for agent-authored changes

## Commands (2)

- `/choose-rail` — Pick and wire the agentic execution framework stack (Superpowers, Spec Kit, GSD, BMAD, built-in) with one owner per slot
- `/modernize` — Plan a legacy system modernization or rebuild with behavior characterization, strategy choice, and verified migration slices

## Evals (4 cases)

Behavioral benchmark in `evals/` (Claude Code `claude plugin eval` format). Each skill has a natural-phrasing trigger case with a method rubric; one negative case must not trigger the plugin.

```
claude plugin eval ./adlc-build
```

---

Part of [ADLC Skills](../README.md). MIT licensed.
