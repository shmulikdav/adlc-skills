---
name: hallucination-checks
description: "Verify that what an agent referenced actually exists and behaves as claimed: packages and versions, imports, API methods, config keys, CLI flags, environment variables, file paths, and documentation links; detect typosquatted or nonexistent dependencies. Use before merging agent-generated code, when a build fails on an unknown symbol, or when adding dependencies an agent suggested."
---

# Hallucination Checks

## Purpose

Plausible-but-nonexistent references are a signature failure of generated code. Some are just broken builds; nonexistent package names are a supply-chain risk, because an attacker can register the name an agent tends to invent.

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
