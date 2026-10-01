# Eval results

How each plugin performs against a no-plugin baseline, measured with `claude plugin eval`. Results are updated as plugins are measured. Re-run any of them: `claude plugin eval ./adlc-<plugin> --model haiku --judge-model sonnet`.

## Status by plugin

| Plugin | Status | Skills with a clear gain |
| --- | --- | --- |
| adlc-foundations | ✅ Measured (5 runs per arm) | 8 of 8 |
| adlc-govern | ✅ Measured (5 runs per arm) | 4 of 6; 2 being re-measured after fixes |
| adlc-verify | ✅ Measured (3 runs per arm) | 3 of 6; 2 did not auto-trigger |
| adlc-intent, adlc-context, adlc-build, adlc-operate, adlc-agent-engineering | Not yet measured | — |

This table is the single source for which plugins are measured; other docs link here instead of repeating counts.

## adlc-foundations (1 October 2026)

**Setup:** Claude Code 2.1.286 · answering model Claude Haiku · judge Claude Sonnet · 5 runs per arm · each case graded by 4–7 atomic criteria, scored as the fraction met.

| Case | Skill | Skill loaded | With | Without | Δ |
| --- | --- | --- | --- | --- | --- |
| champions | ai-champions-program | 5/5 | 0.97 | 0.20 | +0.77 |
| ai-policy | ai-stance-policy | 5/5 | 0.77 | 0.29 | +0.49 |
| map-workflow | sdlc-to-adlc-mapping | 5/5 | 0.70 | 0.30 | +0.40 |
| nobody-understands-it | comprehension-debt | 5/5 | 0.67 | 0.30 | +0.37 |
| autonomy-per-task | autonomy-levels | 5/5 | 1.00 | 0.65 | +0.35 |
| roles | role-transitions | 5/5 | 0.85 | 0.50 | +0.35 |
| readiness-baseline | adlc-readiness-assessment | 5/5 | 1.00 | 0.67 | +0.33 |
| roi-measurement | adlc-metrics | 5/5 | 0.96 | 0.72 | +0.24 |
| near-miss, unrelated-request | none (negative cases) | 0/20 | 1.00 | 1.00 | — |

**What we learned.**

- Every foundations skill loaded on natural phrasing in all 5 runs, and none loaded on the two negative cases, including the near-miss ("what do the four DORA metrics measure?").
- All eight skills improved answers. The largest gains are on organizational design questions (champions programs, AI policy, workflow mapping), where a model without the kit gives generic advice.
- **The first run overstated the gains.** With one all-or-nothing rubric per case, every baseline scored 0.00 and four skills showed Δ +1.00. Split into atomic criteria, baselines earn partial credit and the honest gains are +0.24 to +0.77.
- **The evals caught a usability bug.** With the old `adlc-readiness-assessment`, Haiku asked for more inputs and never assessed (0.00 with the skill), even when the user said "give me your assessment". The skill now gives a provisional assessment and marks gaps as unknown: 1.00 with the skill.
- **Two gaps to fix next.** `ai-stance-policy` never produced a policy short enough (the "one page" criterion failed in every run, both arms), and `comprehension-debt` never proposed named module owners, one of its own core practices.

## adlc-govern (1 October 2026)

**Setup:** as for foundations: Claude Haiku answering, Claude Sonnet judging, 5 runs per arm, 3–6 atomic criteria per case.

| Case | Skill | Skill loaded | With | Without | Δ |
| --- | --- | --- | --- | --- | --- |
| business-teams-building | citizen-builder-governance | 5/5 | 0.83 | 0.27 | +0.57 |
| permissions-ci | agent-permissions | 5/5 | 0.93 | 0.40 | +0.53 |
| threat-model-ci-agent | agentic-threat-model | 5/5 | 1.00 | 0.63 | +0.37 |
| iso-42001 | ai-compliance-mapping | 5/5 | 0.75 | 0.45 | +0.30 |
| protect-secrets | guardrail-hooks | 0/5 | 0.73 | 0.33 | re-measuring |
| vet-plugin | extension-vetting | 1/5 | 0.10 | 0.30 | −0.20, re-measuring |
| near-miss, unrelated-request | none (negative cases) | 0/20 | 1.00 | 0.95 | — |

**What we learned.**

- Four skills give clear gains on the questions security and platform teams ask: citizen-builder governance, agent permissions, threat modeling, and compliance mapping.
- **`extension-vetting` made answers worse, and not because of its content.** With the kit installed, Haiku saw that a vetting workflow existed and replied "share the link and I'll vet it" with a thin checklist, instead of answering. Without the kit it gave a fuller checklist. The skill and the `/vet-extension` command now give the full framework and decision rule first, then offer to vet the specific extension.
- **`protect-secrets` exposed a skill collision.** The neighboring `agent-permissions` skill answered instead of `guardrail-hooks`. It helped, but missed the point `guardrail-hooks` exists to make: instructions alone are not enforcement. Both skills now make that point, and `guardrail-hooks` triggers on "must never happen, no matter what". The case prompt now says "don't change any files", because the baseline kept trying to write a settings file it had no tool for and ran out of turns.
- "Confirm with counsel or the auditor" failed in all ten `iso-42001` runs, with and without the kit. `ai-compliance-mapping` now states it as part of the required output.

## adlc-verify (1 October 2026)

**Setup:** Claude Code 2.1.286 · answering model Claude Haiku · judge Claude Sonnet · 3 runs per arm · ablation with and without the plugin · each case graded by 5–7 atomic criteria, scored as the fraction met.

| Case | Skill | Skill loaded | With | Without | Δ |
| --- | --- | --- | --- | --- | --- |
| dod | definition-of-done | 3/3 | 0.87 | 0.07 | +0.80 |
| pr-queue | review-capacity | 3/3 | 0.57 | 0.05 | +0.52 |
| new-dependency | hallucination-checks | 3/3 | 0.60 | 0.40 | +0.20 |
| tests-pass-wrong-behavior | behavioral-testing | 3/3 | 0.73 | 0.67 | +0.07 |
| review-agent-diff | agent-code-review | 0/3 | 0.81 | 0.81 | 0.00 |
| tests-from-xray | tests-from-specs | 0/3 | 0.87 | 0.67 | not attributable |
| unrelated-request | none (negative case) | 0/6 | 1.00 | 1.00 | — |

## What we learned

**Organizational procedure is where skills pay off.** Without the kit, Haiku gave generic advice on a definition of done and on an overloaded review queue. With it, answers included evidence requirements, automated versus human gates, ownership, risk tiers and WIP limits.

**Generic code review does not need a skill.** Given a diff with six planted defects, Haiku found most of them without help (0.81) and did not load `agent-code-review`. The skill stays available through the `/review-agent-pr` command, which invokes it explicitly; its auto-trigger value on pasted diffs is unproven.

**`tests-from-specs` is unproven.** The with-plugin arm scored higher, but the skill never loaded, and an earlier run of the same case scored 0.80 in both arms. We do not count it.

**The evals caught a real flaw.** The first version of `hallucination-checks` made answers *worse* (Δ −0.07). With the skill loaded, the model stated as fact that a package did not exist without checking, and it stopped asking whether the dependency was needed. We added a rule against asserting unverified facts, plus explicit necessity and approval steps. Re-measured, Δ moved to +0.20.

## How the eval itself was fixed

Getting trustworthy numbers took four iterations, recorded here because each one is a common trap:

1. **All-or-nothing rubrics saturated.** On Opus, one lenient rubric per case passed in both arms (Δ 0). Fix: 5–7 atomic criteria per case.
2. **A small judge was unreliable.** The default judge failed answers that plainly met criteria. Fix: `--judge-model sonnet`.
3. **Prompts referenced material the sandbox did not have.** "Review this PR" in an empty directory produced "please share the PR" in both arms. Fix: inline the spec, diff and test export, with planted defects to find.
4. **Small samples are noisy.** One baseline run scored 0.00 where its siblings scored 0.60. Treat differences under about 0.2 at 3 runs per arm as unconfirmed.

## Not yet measured

See the status table at the top. Opus results with the current rubrics are also pending; earlier Opus runs used saturated rubrics and are not comparable.
