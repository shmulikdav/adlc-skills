---
name: execution-rail-selection
description: "Use when choosing or combining agentic coding frameworks such as Superpowers, GSD, Spec Kit, BMAD, gstack, or Claude Code's built-in plan mode, when two installed frameworks conflict, or when a team asks which workflow plugin to standardize on."
---

# Execution Rail Selection

## Overview

ADLC Skills deliberately does not ship its own code-execution workflow. Mature, heavily used "rails" already do that well, and generic coding skills add little on top of a strong model: in SWE-Skills-Bench, 39 of 49 public software-engineering skills produced zero pass-rate gain. This skill picks the rail and wires ADLC artifacts (agent-ready specs, tasks, Definition of Done) into it.

**Core rule:** one rail per slot. Two frameworks that both claim planning, or both claim execution discipline, fight over state files and instructions.

## The slots

| Slot | Question it answers | Candidates |
|------|--------------------|-----------|
| Spec / plan | What are we building, in what order? | Spec Kit, Kiro specs, AWS AI-DLC, BMAD, GSD, ADLC `adlc-intent` |
| Execution discipline | How is each unit of work done? (TDD, review, debugging, worktrees) | Superpowers; Claude Code built-in plan mode + official `feature-dev` |
| Review | Is the change right? | Official `pr-review-toolkit` / `code-review`; ADLC `adlc-verify` for spec alignment |
| Security review of code | Is the code vulnerable? | Official `security-guidance` / `claude-security`; Trail of Bits skills |
| Governance of the agent setup | Is the agent itself safe to run? | ADLC `adlc-govern` |

## Decision guide

| Situation | Recommended |
|-----------|-------------|
| Team is new to agents, mixed seniority | Built-in plan mode + `feature-dev`; add ADLC `adlc-intent` for specs. Lowest ceremony |
| Quality problems: code works today, breaks tomorrow | Superpowers for execution discipline (enforced TDD, two-stage review) |
| Multiple agent tools across the org (Copilot, Claude Code, Kiro) | Spec Kit or AI-DLC for the spec slot (tool-agnostic artifacts) |
| Solo builder or small team, long multi-session projects | GSD (context-rot control, milestones) |
| Enterprise, role-based handoffs, compliance traces | BMAD for the spec slot, Superpowers for execution |
| Legacy rebuild | Official `code-modernization` plugin as the execution engine; ADLC `legacy-modernization` for strategy |

## Instructions

1. Inventory what is installed (`/plugin` list, `.claude/`, `.specify/`, `.planning/`, `.gsd/`, `_bmad/`). Flag any slot with two owners.
2. Ask three questions: team size and seniority; main failure today (wrong thing built / broken code / context loss / review overload); single or multiple agent tools.
3. Recommend one owner per slot using the tables. State what to uninstall or disable if slots collide.
4. Wire ADLC artifacts in: where the agent-ready spec lives for that rail, where tasks live, where the Definition of Done is enforced (hook, CI, or the rail's own verification step).
5. Define a 2-week trial with one success metric (rework rate or review time), then decide.

## Red flags

| Thought | Reality |
|---------|---------|
| "Install all of them, more structure is better" | Overlapping rails create conflicting instructions; more loaded skills also means more selection errors and token overhead |
| "We'll pick a framework, then figure out specs" | The spec slot is where most agent failures start; choose it deliberately |
| "The framework replaces review" | Rails structure the work; humans still own alignment and release gates |

## Output

A one-page stack decision: slot → owner → why, collisions resolved, artifact wiring, trial metric.

---

### Further Reading

- [Superpowers](https://github.com/obra/superpowers)
- [Anthropic official plugin directory](https://github.com/anthropics/claude-plugins-official)
- [GitHub Spec Kit](https://github.com/github/spec-kit)
- [AWS AI-DLC workflows](https://github.com/awslabs/aidlc-workflows)
- [SWE-Skills-Bench (arXiv 2603.15401)](https://arxiv.org/abs/2603.15401)
