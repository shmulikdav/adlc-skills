# Eval results

How each plugin performs against a no-plugin baseline, measured with `claude plugin eval`. Results are updated as plugins are measured. Re-run any of them: `claude plugin eval ./adlc-<plugin> --model haiku --judge-model sonnet`.

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

adlc-foundations, adlc-intent, adlc-context, adlc-build, adlc-govern, adlc-operate, adlc-agent-engineering. Opus results with the current rubrics are also pending; earlier Opus runs used the saturated rubrics and are not comparable.
