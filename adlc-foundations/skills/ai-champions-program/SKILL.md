---
name: ai-champions-program
description: "Design an internal AI Champions / AI Enablers program (train-the-trainer) that spreads agentic development practices across engineering teams: champion selection, enablement curriculum, office hours, shared skills library, cadence, and success metrics. Use when a company wants to scale Claude Code or Cursor adoption beyond early adopters, build an AI enablers community, or set up train-the-trainer for ADLC."
---

# AI Champions Program

## Purpose

Tools spread by licence; practices spread by people. A champions network turns a few strong practitioners into a distribution channel for context files, skills, and working patterns.

## Program design

1. **Charter (one paragraph):** goal, scope (which teams), time horizon, executive sponsor.
2. **Champion profile:** respected engineer or PM, already productive with agents, willing to spend ~10–15% of time; one per team of 6–10.
3. **Selection:** nomination by team leads plus a short practical task (e.g., ship one agent-built PR with a written spec and tests).
4. **Curriculum (4 modules):**
   - Intent: writing agent-ready specs and acceptance criteria
   - Context: maintaining CLAUDE.md/AGENTS.md, codifying conventions as skills
   - Verification: tests-first with agents, reviewing for alignment
   - Governance: permissions, secrets, extension vetting
5. **Rituals:** bi-weekly champions sync; monthly show-and-tell; office hours per team.
6. **Shared assets:** an internal plugin/skills repo owned by the champions, with a contribution process.
7. **Feedback loop:** champions collect failure cases and turn them into context-file updates or new skills.

## Output

```
## AI Champions Program: [Company]
### Charter
### Champion roster template (team | champion | backup | start date)
### 8-week launch plan (week-by-week)
### Curriculum outline with exercises
### Shared skills repo: structure and contribution rules
### Success metrics (adoption, rework rate, # shared skills used, NPS of enablement)
### Risks and mitigations
```

## Notes

- Give champions recognized time and visibility; unpaid side-jobs fade in two months.
- Measure what champions change (team rework rate, spec quality), not how many sessions they ran.
- Rotate champions yearly to avoid single points of knowledge.

---

### Further Reading

- [DORA AI Capabilities Model](https://dora.dev/research/publications/)
