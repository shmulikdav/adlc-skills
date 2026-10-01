---
name: spec-driven-development
description: "Run Spec-Driven Development (SDD) for agentic coding: constitution (project principles) → specify (what and why) → clarify → plan (how) → tasks → implement → converge, with each artifact versioned in the repo. Use when a team wants a structured spec-first workflow for coding agents, mentions GitHub Spec Kit, Kiro specs, or AWS AI-DLC, or wants to move from vibe coding to repeatable delivery."
---

# Spec-Driven Development (SDD)

## Purpose

In SDD the specification, not the prompt, is the durable source of truth. Agents implement against versioned artifacts; humans review the artifacts at each gate. This skill runs the loop in a tool-agnostic way and maps it to popular implementations.

## The loop

| Stage | Artifact | Human gate |
|-------|----------|-----------|
| Constitution (once per project) | `constitution.md`: non-negotiable principles (testing, security, architecture, style) | Tech lead approves |
| Specify | `specs/<feature>/spec.md`: what and why, no tech choices | PM/owner approves |
| Clarify | Updated spec, open questions resolved | Owner confirms |
| Plan | `plan.md` (+ data-model, contracts, research): the how, checked against the constitution | Tech lead approves |
| Tasks | `tasks.md`: small, ordered, dependency-aware, parallel tasks marked | Quick review |
| Implement | Code + tests per task | PR review for alignment |
| Converge | Spec/plan updated to match what was actually built | Owner signs off |

## Instructions

1. **Detect the toolchain.** If `.specify/` exists, follow GitHub Spec Kit conventions. If `.kiro/specs/` exists, follow Kiro (requirements.md, design.md, tasks.md). If AWS AI-DLC rules are present, follow Inception → Construction. Otherwise create `specs/<feature>/` with the artifacts above.
2. **Constitution first.** If none exists, draft 5–9 principles from the repo (test commands, architecture patterns, banned practices) and ask for approval.
3. **Specify** without technology. If the user mixes in tech choices, move them to the plan.
4. **Clarify** using the spec-clarification method before planning; never plan on top of unresolved ambiguity that affects behavior.
5. **Plan** and run a constitution check: list each principle and whether the plan complies; justify any exception.
6. **Tasks**: 1–4 hour units, each with a verification step, mark independent tasks `[P]`, order by dependency (tests before implementation where possible).
7. **Implement** task by task; after each, run the verification and tick the task.
8. **Converge**: diff the shipped behavior against spec.md; update docs so the spec stays true.

## Output

The artifact set in the repo, plus a short status summary listing which gates are approved and which are pending.

## Notes

- SDD adds overhead. Use it for features with real ambiguity or risk; a one-line fix does not need a constitution check.
- Never let an agent self-approve a gate. Gates exist to put human judgment at the points where it matters most.

---

### Further Reading

- [GitHub Spec Kit](https://github.com/github/spec-kit)
- [AWS AI-DLC workflows](https://github.com/awslabs/aidlc-workflows)
