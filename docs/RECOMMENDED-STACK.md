# Recommended ADLC Stack

ADLC Skills is the operating-model layer. Pair it with the best execution and security plugins. One owner per slot; don't install two frameworks that claim the same slot.

## Default stack (most teams)

| Slot | Install | From |
|------|---------|------|
| Operating model, specs, governance | `adlc-foundations`, `adlc-intent`, `adlc-govern` | `shmulikdav/adlc-skills` |
| Execution discipline | `superpowers` | `claude-plugins-official` |
| PR review | Built-in `/code-review` (and `/ultrareview` for critical changes), `pr-review-toolkit`, plus `adlc-verify` for spec alignment and review-capacity design | built-in + official + this repo |
| Background agents | GitHub Agentic Workflows or Claude Code routines, designed with `adlc-operate` | GitHub / built-in + this repo |
| Code security | `security-guidance` | `claude-plugins-official` |
| Context upkeep | `claude-md-management` + `adlc-context` | official + this repo |

```bash
claude plugin marketplace add shmulikdav/adlc-skills
claude plugin install adlc-foundations@adlc-skills
claude plugin install adlc-intent@adlc-skills
claude plugin install adlc-govern@adlc-skills
claude plugin install adlc-verify@adlc-skills
claude plugin install adlc-context@adlc-skills
claude plugin install superpowers@claude-plugins-official
claude plugin install pr-review-toolkit@claude-plugins-official
claude plugin install security-guidance@claude-plugins-official
claude plugin install claude-md-management@claude-plugins-official
```

Verify names with `/plugin` before installing; marketplaces evolve.

## Variants

| Team shape | Swap in |
|------------|---------|
| Several agent tools across the org (Copilot, Kiro, Claude Code) | Spec Kit or AWS AI-DLC for the spec slot; keep `adlc-intent` for agent-ready PRDs |
| Solo builder, long multi-session projects | GSD instead of Superpowers |
| Enterprise with role-based handoffs | BMAD for the spec slot, Superpowers for execution |
| Legacy rebuild | Official `code-modernization` for execution, `adlc-build` for strategy |
| Security-critical codebase | Add Trail of Bits skills (CodeQL, Semgrep, property-based testing, supply-chain auditor) |
| Building agent products | `adlc-agent-engineering` + `adlc-operate` |

## Do not combine

- Superpowers + GSD + BMAD all as full rails.
- Two spec systems writing to different state folders (`.specify/`, `.planning/`, `.gsd/`).
- Every plugin from every marketplace: more loaded skills means more selection errors and token overhead.
