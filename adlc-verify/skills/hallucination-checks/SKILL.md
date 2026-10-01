---
name: hallucination-checks
description: "Use before merging agent-generated code, when a build fails on an unknown symbol, package, or flag, when an agent adds or suggests a new dependency, or when PR text claims results without evidence."
---

# Hallucination Checks

**Grounded in:** Spracklen et al.: package hallucinations by code-generating LLMs; OpenSSF: Security-Focused Guide for AI Code Assistant Instructions; NIST SP 800-218A: SSDF Community Profile for Generative AI.





## Purpose

Plausible-but-nonexistent references are a signature failure of generated code. Research on package hallucinations (Spracklen et al.) found code-generating models regularly recommend packages that don't exist, which attackers can register ("slopsquatting"). Some are just broken builds; nonexistent package names are a supply-chain risk, because an attacker can register the name an agent tends to invent.

## Checklist

1. **Dependencies:** for every new or changed dependency, confirm it exists on the official registry, check the exact name (typosquats), publisher, download history, last release date, and licence. Pin versions.
2. **Imports & symbols:** confirm each imported module and called function exists in the installed version (type-check, compile, or inspect the package source).
3. **APIs:** for external APIs, confirm endpoints, parameters, and response fields against current official docs or the SDK types.
4. **Config & flags:** confirm config keys, environment variables, and CLI flags exist and are spelled as the tool expects.
5. **Paths & links:** confirm referenced files exist; confirm documentation URLs resolve.
6. **Claims in PR text:** "tests pass", "no breaking changes", "performance improved" must be backed by output in the PR.

## Instructions

Run what can be run (install, build, type-check, tests). For what can't be run, check against authoritative sources. Report each reference as `verified`, `not found`, or `unverifiable` with the evidence.

## Output

`| Reference | Type | Status | Evidence | Action |`

## Notes

- Treat a new dependency suggested by an agent as a supply-chain decision requiring human approval.

---

### Further Reading
- [Spracklen et al.: package hallucinations by code-generating LLMs](https://arxiv.org/abs/2406.10279)
- [OpenSSF: Security-Focused Guide for AI Code Assistant Instructions](https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions)
- [NIST SP 800-218A: SSDF Community Profile for Generative AI](https://csrc.nist.gov/pubs/sp/800/218/a/final)
