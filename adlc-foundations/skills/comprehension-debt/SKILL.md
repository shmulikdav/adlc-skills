---
name: comprehension-debt
description: "Use when teams ship code faster than they understand it, nobody can explain or debug agent-written modules, juniors learn mostly through AI, incident response slows on AI-built code, or leaders worry about skill atrophy and the long-term ability to verify agent output."
---

# Comprehension Debt

**Grounded in:** Anthropic Research: How AI assistance impacts the formation of coding skills; Thoughtworks Technology Radar (Vol. 34, April 2026).





## Overview

Comprehension debt is the gap between the code a team owns and the code it actually understands. It hides behind green tests until the first serious incident. In Anthropic's 2026 randomized trial, developers learning a new library with AI assistance scored 17% lower on comprehension (50% vs 67%), with debugging hit hardest; but those who used AI for conceptual questions rather than delegation preserved most of their learning. How AI is used matters more than whether it is used.

**Core rule:** every merged change has at least one human who can explain it, debug it, and change it without the agent.

## Practices

| Practice | What it looks like | Targets |
|----------|--------------------|---------|
| Explain-back gate | Before merge, the requester explains the change's approach and risks in the PR, in their own words | Ownership of agent output |
| Conceptual-inquiry mode | For unfamiliar tech, use the agent to explain and quiz, not to write | Learning, juniors |
| Ownership map | Each module has a named human owner who has read it end to end | Bus factor |
| Agent-off reps | Periodic tasks (debugging drills, design katas) without AI | Skill retention |
| Incident readiness | Game days on agent-built components | Debuggability |
| Design reviews stay human | Architecture decisions are discussed by people, recorded as ADRs | System understanding |

## Instructions

1. **Assess:** for the top 10 critical modules, can a named person explain and debug each without AI? Where did the last incidents take longest to diagnose?
2. **Identify hot spots:** modules with high agent authorship, low human edits, and no clear owner.
3. **Choose practices** proportionate to risk; apply the explain-back gate to high-tier changes first.
4. **Protect juniors:** set an expectation of conceptual-inquiry use for learning tasks; pair them on review and spec writing.
5. **Track:** time-to-diagnose incidents, owner coverage of critical modules, and survey-based confidence in explaining owned code.

## Red flags

| Thought | Reality |
|---------|---------|
| "Tests pass, so we understand it" | Tests check behavior; understanding is what you need when tests don't cover the failure |
| "The agent can explain it later" | During an incident you need humans who already know |
| "Juniors are productive, so they're learning" | Output and skill formation are different measurements |

## Output

Comprehension-debt assessment (module × owner × explainability), chosen practices, and tracking metrics.

---

### Further Reading

- [Anthropic Research: How AI assistance impacts the formation of coding skills (2026)](https://www.anthropic.com/research/AI-assistance-coding-skills)
- [Addy Osmani: Comprehension debt](https://addyosmani.com/blog/comprehension-debt/)
- [Thoughtworks Technology Radar (Vol. 34, April 2026)](https://www.thoughtworks.com/radar)
