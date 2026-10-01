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
6. **Necessity:** before vetting a new dependency, ask whether it is needed at all. Can an existing dependency or the standard library do the job? Every new package is permanent attack surface.
7. **Approval and pinning:** a new dependency is a human decision, not an agent's. Require explicit approval, pin the exact version, and commit the lockfile.
8. **Claims in PR text:** "tests pass", "no breaking changes", "performance improved" must be backed by output in the PR.

## The rule this skill must follow itself

Never state that something exists or does not exist unless you checked it in this session. If you cannot reach the registry or docs (no network, no shell), say so plainly, mark the reference **unverified**, and give the exact commands for a human to check it, for example `npm view <package> name version time maintainers repository`, `pip index versions <package>`, or the package page URL. Flagging a name as *suspicious* is fine; declaring it *nonexistent* without evidence is the same failure this skill exists to catch.

## Instructions

Run what can be run (install, build, type-check, tests). For what can't be run, check against authoritative sources. Report each reference as `verified`, `not found`, or `unverified` with the evidence; `not found` requires an actual lookup.

## Output

`| Reference | Type | Status | Evidence | Action |`

For a new dependency, end with a decision line: needed or not, approved by whom, version pinned, lockfile committed.

## Notes

- Treat a new dependency suggested by an agent as a supply-chain decision requiring human approval.

---

### Further Reading
- [Spracklen et al.: package hallucinations by code-generating LLMs](https://arxiv.org/abs/2406.10279)
- [OpenSSF: Security-Focused Guide for AI Code Assistant Instructions](https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions)
- [NIST SP 800-218A: SSDF Community Profile for Generative AI](https://csrc.nist.gov/pubs/sp/800/218/a/final)
