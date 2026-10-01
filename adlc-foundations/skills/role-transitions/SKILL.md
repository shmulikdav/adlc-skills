---
name: role-transitions
description: "Use when leaders ask how developer, PM, QA, tech lead, manager, or designer roles change with coding agents, when updating career ladders or job descriptions for agentic development, or when people worry what their job becomes."
---

# Role Transitions in the ADLC

**Grounded in:** Anthropic: 2026 Agentic Coding Trends Report; Anthropic Research: How AI assistance impacts the formation of coding skills.





## Purpose

When execution moves to agents, the scarce skills become specifying intent, curating context, and verifying output. This skill makes role changes explicit so people know what "good" looks like now.

## Reference shifts

| Role | Less of | More of | New core skill |
|------|---------|---------|----------------|
| Developer | Typing implementation | Decomposing work, reviewing diffs for alignment, owning tests | Orchestrating agents; judging correctness fast |
| Product manager | Ticket grooming | Writing agent-ready specs with testable acceptance criteria; prototyping | Intent specification |
| QA | Manual regression | Designing behavioral tests and eval suites; owning the verification harness | Test strategy for non-deterministic output |
| Tech lead | Line-by-line review | Architecture constraints, context files, gates, autonomy levels | Governance of agent work |
| Eng manager | Capacity planning by headcount | Measuring outcomes and rework; coaching on new workflows | Managing a hybrid human+agent system |
| Designer | Static handoff | Design systems and tokens agents can consume; rapid prototype review | Machine-readable design intent |

## Instructions

1. Ask which roles exist and their current responsibilities.
2. For each role produce: stop / start / continue; required skills; a 90-day development plan; and updated performance signals (e.g., for developers: rework rate of merged changes, quality of specs and tests, not lines of code).
3. Flag risks: junior developers losing learning opportunities; review fatigue; unclear ownership of agent-produced code.

## Output

One section per role with the structure above, plus a short "what stays the same" note so the change does not feel like erasure.

## Notes

- Accountability does not move to the agent. The person who merges owns the outcome.
- Protect junior growth deliberately: pair them on spec writing and review, not only on prompting. See the comprehension-debt skill for practices backed by Anthropic's 2026 skill-formation study.

---

### Further Reading

- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
- [Anthropic: 2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report)
- [Anthropic Research: How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)
