---
name: sdlc-to-adlc-mapping
description: "Use when redesigning a development process around coding agents, explaining SDLC vs ADLC to managers, deciding where agents should enter an existing workflow first, or when a team asks what changes in each lifecycle stage when agents do the work."
---

# SDLC → ADLC Mapping

## Purpose

The ADLC keeps the familiar lifecycle stages and changes who executes them. This skill makes that shift concrete for a specific team so leaders can see where agents add leverage, where humans must stay, and where new risks enter.

## The core shift

| Dimension | SDLC | ADLC |
|-----------|------|------|
| Who builds | Humans write deterministic code | Agents execute; humans specify intent and constraints |
| Primary artifact | Code | Spec + context + code + tests, produced together |
| What is reviewed | Code correctness | Behavioral alignment with intent |
| How it fails | Bugs: predictable, traceable | Plausible-but-wrong output: confident, invisible |
| What governs | Linters, PR review, CI | Context files, permissions, hooks, evals, gates |
| Cadence | Sprints | Short "bolts" of hours to days, gated by human approval |
| Bottleneck | Writing code | Specifying intent and verifying output |

## Instructions

1. **Capture the current flow.** List each step from idea to production. For each: owner role, input, output artifact, tool, typical duration, and pain point.
2. **Map each step** using this table:

```
| SDLC step | ADLC executor (Human / Agent / Pair) | New artifact | Human gate kept | New failure mode | Guardrail |
```

Typical mappings:
- Requirements → **Intent specification** (agent-ready PRD with acceptance criteria). Human owns intent.
- Design → **Architecture as constraint** (ADRs, context files the agent must follow).
- Implementation → **Agent execution** inside a plan, with rules files and permissions.
- Testing → **Behavioral validation** (tests derived from the spec, run by the agent, checked by a human).
- Code review → **Alignment review** (does the diff match the spec, not just "does it compile").
- Release → **Gated deployment** with explicit human approval.
- Operations → **Observability + learning loop** (agent failures feed back into context files).

3. **Pick entry points.** Rank steps by (pain × agent suitability × verifiability). Agents should enter first where output is cheap to verify: test generation, refactors with good coverage, docs, migrations with clear before/after.
4. **Name the new roles.** Who writes specs, who curates context files, who owns gates.

## Output

The mapping table, a ranked list of the first three entry points with rationale, and a "what changes for each role" section (PM, developer, QA, team lead). Save as `SDLC-to-ADLC-[team]-[date].md`.

## Notes

- Do not remove a human gate without a replacement verification mechanism.
- A step an agent can do but nobody can verify is not ready for delegation.
- Most organizations run SDLC and ADLC side by side for a long time. Plan for coexistence.

---

### Further Reading

- [AWS AI-DLC workflows (open-source rules: Inception, Construction, Operations)](https://github.com/awslabs/aidlc-workflows)
- [EPAM: Agentic Development Lifecycle explained](https://www.epam.com/insights/ai/blogs/agentic-development-lifecycle-explained)
- [Cycode: Agentic Development Lifecycle (ADLC)](https://cycode.com/blog/agentic-development-lifecycle-adlc/)
