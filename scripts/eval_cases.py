#!/usr/bin/env python3
"""Source of truth for the plugin eval suites (Claude Code `claude plugin eval` format).

Each case: realistic prompt (never names the skill) + a `tool_used: Skill` indicator grader
+ an `llm` rubric that rewards the skill's method (what a no-plugin baseline usually misses).
Each plugin also gets negative cases that must NOT trigger the plugin's skills.

Regenerate with:  python3 scripts/eval_cases.py
"""
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CASES = {
"adlc-foundations": [
 ("readiness-baseline", "adlc-readiness-assessment",
  "We're a 40-person engineering org. Everyone got Claude Code licences two months ago but nobody can tell me if it's working. Deploys are weekly, coverage is about 35%, there's no written AI policy, and PRs sit in review for days. Are we actually ready to scale agents? Give me your assessment.",
  "PASS if the response scores readiness across organizational capabilities (e.g., AI policy/stance, version control, small batches, internal platform, data access) and agent-specific readiness (context files, verification/tests, governance), assigns a maturity level justified by the weakest critical dimensions rather than an average, and lists concrete first moves. FAIL if it only gives generic tool tips or a generic pros/cons list without a scored assessment."),
 ("autonomy-per-task", "autonomy-levels",
  "Can we let the coding agent handle dependency bumps, CRUD endpoints, and database schema migrations on its own, without a human reviewing every PR?",
  "PASS if the response treats each task type separately, rates them on factors like blast radius, reversibility, and verifiability, assigns a different autonomy level or approval requirement to schema migrations than to dependency bumps, and states criteria for promoting or demoting autonomy. FAIL if it gives one blanket yes/no answer for all three."),
 ("roi-measurement", "adlc-metrics",
  "My VP wants proof that Cursor and Claude Code are paying off. The devs say they're 30% faster. How should I measure this?",
  "PASS if the response warns that self-reported speedups are unreliable, requires a baseline and a comparison design, includes stability or rework metrics alongside throughput (e.g., change-failure rate, rework or revert rate), and defines attribution of agent-authored changes. FAIL if it accepts the 30% claim or proposes vanity metrics like lines of code or number of prompts as the main measure."),
],
"adlc-intent": [
 ("vague-ticket-to-spec", "agentic-prd",
  "I want to hand this ticket to Claude Code: 'Let admins export audit logs.' Turn it into something the agent can build without guessing.",
  "PASS if the response produces a spec with explicit non-goals or out-of-scope items, constraints or guardrails, testable acceptance criteria, and conditions under which the agent must stop and ask, and it raises or labels assumptions about format, filters, permissions, or data size. FAIL if it simply restates the ticket as a longer user story without non-goals, acceptance criteria, or stop conditions."),
 ("criteria-from-story", "acceptance-criteria",
  "Write acceptance criteria for: 'Users can upload a profile photo.' Our agent will generate tests from them.",
  "PASS if the criteria are in Given/When/Then or EARS form, include at least one negative path (e.g., oversized or wrong-type file) and a boundary with a concrete number, and state how each criterion is verified. FAIL if criteria are vague (e.g., 'upload works smoothly') or only cover the happy path."),
 ("interview-me", "spec-clarification",
  "Here's my spec: 'Bulk user import from CSV. Admins upload a file and users get created.' What's missing before an agent builds it?",
  "PASS if the response surfaces silent decisions such as duplicates, validation and partial failure, file size limits, permissions, existing-user handling, and notifications, prioritizes them, and gives a recommended default for each question. FAIL if it lists generic questions with no prioritization and no defaults."),
],
"adlc-context": [
 ("bloated-claude-md", "agent-context-files",
  "Our CLAUDE.md is 700 lines — architecture essays, style rules, onboarding docs, everything. Claude seems to ignore half of it. How should we fix it?",
  "PASS if the response recommends cutting content the agent can derive from code, keeping commands, non-default conventions, boundaries, and verification steps, moving area-specific rules to nested files or linked docs, and treating the file like code that gets reviewed and pruned. FAIL if it suggests adding more instructions or emphasis (e.g., capital letters) as the main fix."),
 ("convention-to-enforcement", "codify-conventions",
  "The agent keeps editing our already-applied database migration files even though CLAUDE.md says not to. What should we do?",
  "PASS if the response says this rule should be enforced deterministically (a hook, permission deny rule, CI check, or test) rather than relying on more instructions, and explains why instructions alone are insufficient. FAIL if it only suggests rewording or repeating the instruction in CLAUDE.md."),
 ("prune-skills", "skill-library-management",
  "We've collected about 60 skills from various GitHub repos into our team's Claude Code setup. Things feel slower and the agent does odd extra work sometimes. How do we decide what to keep?",
  "PASS if the response recommends measuring each skill against a no-skill baseline (or equivalent evals), cutting generic skills that restate what the model already does or duplicate others, fixing descriptions so they state when to use the skill, and keeping a smaller focused set. FAIL if it recommends keeping everything or adding more skills."),
],
"adlc-build": [
 ("which-framework", "execution-rail-selection",
  "We installed both Superpowers and GSD plus Spec Kit and now Claude gets confused about which plan to follow. What setup should we standardize on?",
  "PASS if the response identifies that multiple frameworks are competing for the same responsibility (planning/spec vs execution discipline), recommends one owner per responsibility, and says what to remove or disable. FAIL if it recommends keeping all three as-is or picks one without explaining the overlap."),
 ("huge-agent-prs", "small-batch-delivery",
  "Our agents open 2,000-line PRs and reviewers just rubber-stamp them. How do we fix this?",
  "PASS if the response sets a PR size budget, recommends splitting into stacked or sequential PRs, uses feature flags or trunk-based integration, and requires rollback readiness or a review contract in the PR description. FAIL if it only suggests reviewers 'be more careful' or adding more AI review."),
 ("legacy-rebuild", "legacy-modernization",
  "We want Claude Code to rebuild our 12-year-old PHP billing dashboard in TypeScript. How should we approach it?",
  "PASS if the response requires capturing current behavior first (characterization or golden tests, recorded inputs/outputs), compares strangler-fig with full rewrite, migrates in slices with parity checks, and requires an owner to confirm billing or money rules rather than inferring them from code. FAIL if it jumps straight to having the agent translate the code file by file."),
],
"adlc-verify": [
 ("review-agent-diff", "agent-code-review",
  "Claude Code wrote a PR that adds rate limiting to our public API. The tests pass and the code looks clean. What should I check before approving?",
  "PASS if the response checks alignment against the spec (scope creep and omissions), whether tests were modified or weakened in the same PR, and AI-specific failure patterns (invented APIs or config, swallowed errors, duplicated helpers), plus security on the new paths. FAIL if it only lists generic code review tips."),
 ("new-dependency", "hallucination-checks",
  "The agent added a package called 'fast-json-sanitizerx' to our package.json to fix a parsing bug. Anything I should do before merging?",
  "PASS if the response says to verify the package actually exists on the official registry, checks for typosquatting or slopsquatting, publisher, history and licence, and treats the dependency as a supply-chain decision needing human approval. FAIL if it simply explains how to use or install the package."),
 ("tests-from-xray", "tests-from-specs",
  "We have 140 test cases in Xray for checkout and maybe half have automated tests. How can an agent help close the gap?",
  "PASS if the response builds traceability between test cases or acceptance criteria and existing tests, classifies verified vs proposed vs gap, keeps Xray IDs in test names or annotations, and only marks items verified after running tests. FAIL if it just suggests generating lots of tests without traceability."),
],
"adlc-govern": [
 ("threat-model-ci-agent", "agentic-threat-model",
  "We're about to run Claude Code in CI with access to our GitHub and Jira through MCP so it can pick up tickets and open PRs. What could go wrong?",
  "PASS if the response covers prompt injection or goal hijack via untrusted ticket/issue content, over-broad tool permissions and credential scope, supply chain of MCP servers, and code execution outside a sandbox, and proposes concrete controls (least privilege, scoped tokens, approvals, hooks, audit logs). FAIL if it only discusses generic CI security without agent-specific risks."),
 ("vet-plugin", "extension-vetting",
  "Someone on the team found a cool Claude Code plugin on GitHub with hooks and an MCP server. Is it safe to install?",
  "PASS if the response distinguishes instruction-only content from executable content (hooks, scripts, MCP servers), says to read every skill and script before installing, looks for exfiltration, remote code fetching, secret access, or instruction-override patterns, checks provenance and version pinning, and ends with an install, restrict, or reject decision framework. FAIL if it says it's probably fine because it's popular."),
 ("protect-secrets", "guardrail-hooks",
  "How do I make sure the agent never edits our .env files or CI workflows, no matter what?",
  "PASS if the response recommends deterministic enforcement such as a PreToolUse hook and/or permission deny rules that block edits to those paths, and explains that instructions alone are not reliable. FAIL if the only advice is to add a line to CLAUDE.md."),
],
"adlc-operate": [
 ("agent-postmortem", "agent-incident-review",
  "An agent refactor dropped a database index last week and checkout latency spiked for 40 minutes. Can you help me run the postmortem?",
  "PASS if the response reconstructs a timeline from transcripts and logs, analyzes which layer let the failure through (spec, context, permissions, verification, gates), stays blameless, and turns findings into durable artifacts (hook, test, eval case, permission or gate change) with owners. FAIL if it concludes 'the AI made a mistake' or only recommends being more careful."),
 ("ai-spend", "ai-cost-management",
  "Our token bill tripled this quarter and finance is asking questions. Where do I start?",
  "PASS if the response establishes cost attribution by team or workflow, computes unit costs (per run, per merged change, or per outcome), identifies top drivers, and proposes levers (model routing, caching, context trimming, step limits) each with a quality guardrail. FAIL if it only suggests switching to a cheaper model."),
 ("go-no-go", "release-gates",
  "This release has an agent-built audit export feature and a billing migration. What should the go/no-go look like?",
  "PASS if the response classifies changes by risk, requires explicit human approval for the billing migration, defines progressive rollout and concrete rollback triggers, and lists the evidence each gate needs. FAIL if it treats both changes the same."),
],
"adlc-agent-engineering": [
 ("should-it-be-an-agent", "agent-architecture",
  "We want an AI agent that reads support tickets, checks order status in our API, and issues refunds under $50. How should we architect it?",
  "PASS if the response considers simpler workflow patterns before a fully autonomous agent, defines tools and autonomy boundaries, requires human approval or strong controls for refunds, and includes stop conditions and an eval plan. FAIL if it jumps to a fully autonomous multi-agent system without justification."),
 ("evals-for-agent", "eval-suite-design",
  "How do we know if our support agent got better or worse when we change the prompt or upgrade the model?",
  "PASS if the response proposes an eval suite built from real cases and failures, uses multiple grader types (code-based, model-based, human calibration), separates capability from regression evals, runs multiple trials, and gates releases on regression results. FAIL if it suggests manually spot-checking a few conversations."),
 ("injection-defense", "agent-runtime-guardrails",
  "Our agent reads customer emails and can update orders. A red-teamer got it to change a shipping address by putting instructions in an email. How do we fix this?",
  "PASS if the response treats email content as untrusted data (provenance labeling), validates tool arguments, requires human approval for high-impact actions like address changes, limits tool permissions, and adds the attack as a regression eval case. FAIL if the only fix is a stronger system prompt telling the agent to ignore instructions."),
],
}

NEGATIVE = {
"adlc-foundations": "What's the difference between a Python list and a tuple?",
"adlc-intent": "Fix the typo in this sentence: 'The fucntion returns teh value.'",
"adlc-context": "Convert 72 degrees Fahrenheit to Celsius.",
"adlc-build": "Write a regex that matches US ZIP codes.",
"adlc-verify": "Explain what a closure is in JavaScript in two sentences.",
"adlc-govern": "What's a good name for a golden retriever puppy?",
"adlc-operate": "Summarize the plot of Romeo and Juliet in three sentences.",
"adlc-agent-engineering": "How many days are there in a leap year?",
}

EXTRA = {
"adlc-foundations": [
 ("map-workflow", "sdlc-to-adlc-mapping",
  "Our flow is: PM writes a Confluence spec, dev implements, PR review, QA tests manually, weekly release. Where should coding agents come into this, and what changes at each step?",
  "PASS if the response maps each step to who executes it with agents (human, agent, or both), names the human gate kept at each step and a new failure mode agents introduce, and ranks where agents should enter first based on how verifiable the output is. FAIL if it gives a generic list of AI tools per step without gates or failure modes."),
 ("ai-policy", "ai-stance-policy",
  "Developers keep asking whether they're allowed to paste customer logs into Claude or let it push to branches. We need an AI policy for engineering. Draft it.",
  "PASS if the draft is short, covers approved tools, data rules for what may and may not go into prompts, what agents may do versus what requires a human, code ownership by the human who merges, and how extensions such as MCP servers or plugins are approved, and flags items for legal review. FAIL if it is a long generic ethics statement without operational rules."),
 ("champions", "ai-champions-program",
  "We bought licences for everyone but only 10% of engineers use agents seriously. How do we spread the practices?",
  "PASS if the response proposes a champions or train-the-trainer network with selection criteria, recognized time allocation, a curriculum covering specs, context, verification and governance, a shared skills or plugin library, and outcome metrics rather than session counts. FAIL if it only suggests more training webinars."),
 ("roles", "role-transitions",
  "How does the QA engineer's job change when agents write most of the code and tests?",
  "PASS if the response says what QA does less of and more of, highlights designing behavioral tests or eval suites and owning the verification harness, and proposes new performance signals. FAIL if it claims QA is no longer needed or gives only generic encouragement."),
],
"adlc-intent": [
 ("spec-first-flow", "spec-driven-development",
  "We keep vibe coding features with Claude and they fall apart. I want a spec-first process the agent follows, with approvals in the right places. Set it up for our next feature: real-time order status notifications.",
  "PASS if the response establishes project principles (a constitution or equivalent), separates the what/why spec from the technical plan, requires clarifying ambiguities before planning, produces tasks, and names explicit human approval gates. FAIL if it goes straight to an implementation plan or code."),
 ("break-down", "task-decomposition",
  "Here's the plan: add CSV export for audit logs — new API endpoint, background job for large exports, email when ready, admin UI button. Break it into tasks for agents.",
  "PASS if tasks are small and individually verifiable, each with files or area touched and a done check, dependencies are explicit, independent tasks are marked as parallelizable, and requirements are traced to tasks. FAIL if it is a flat to-do list without dependencies or done checks."),
],
"adlc-context": [
 ("map-repo", "codebase-map",
  "We're about to have agents work in a 9-year-old monolith nobody fully understands. What should we produce first so agents and new people can navigate it?",
  "PASS if the response proposes a structured map with module responsibilities, entry points, core flows traced end to end, change recipes for common modifications, and a risk register, kept as a linked doc rather than pasted into the context file. FAIL if it only says to read the README or add more comments."),
 ("context-rot", "context-budget",
  "In long Claude Code sessions the agent starts forgetting instructions and redoing work. What are we doing wrong?",
  "PASS if the response explains that context fills and quality degrades, recommends one task per session with clearing between tasks, delegating exploration to subagents, externalizing state into plan or progress files for handoff, and moving rarely-needed material out of always-loaded context. FAIL if it only recommends writing longer or more forceful instructions."),
 ("mcp-plan", "mcp-integration-plan",
  "Which of our systems should Claude Code connect to through MCP? We have Jira, Confluence, Figma, Datadog, and a Postgres production database.",
  "PASS if the response prioritizes by value and risk, starts read-only with scoped access, flags production database write access as requiring a human gate or exclusion, notes prompt-injection risk from sources with third-party or user-generated text, and proposes a rollout order. FAIL if it recommends connecting everything with full access."),
],
"adlc-verify": [
 ("tests-pass-wrong-behavior", "behavioral-testing",
  "Our agent-written tests all pass, but last week an invoice total came out wrong in production. How should we test agent-built billing code differently?",
  "PASS if the response recommends testing properties and invariants (e.g., totals equal sum of lines, no negative balances), contract or state-transition tests, and tests designed to fail on a plausible wrong implementation, rather than tests mirroring the implementation. FAIL if it only says to write more unit tests."),
 ("dod", "definition-of-done",
  "Our agents keep saying 'done' when things are half-finished. What standard should we hold them to?",
  "PASS if the response defines a checklist requiring fresh evidence (test output, type check, lint) attached before claiming completion, separates automatable checks from human gates, and suggests enforcing it via hooks or CI. FAIL if it only suggests asking the agent to double-check its work."),
],
"adlc-govern": [
 ("permissions-ci", "agent-permissions",
  "What should Claude Code be allowed to do without asking on developer laptops versus in our CI pipeline?",
  "PASS if the response classifies actions into allow, ask, and deny, defines separate local and CI profiles with CI being narrower and sandboxed with scoped tokens, denies reading secrets files and pushing to main, and recommends backing critical rules with hooks. FAIL if it recommends one permissive setting everywhere."),
 ("iso-42001", "ai-compliance-mapping",
  "We're going for ISO 42001 and SOC 2, and auditors will ask how we govern AI coding agents. What do we need to show?",
  "PASS if the response maps expectations from the named frameworks to current practices, identifies gaps, and lists concrete evidence artifacts (policy, risk register or threat model, permission configs, review records, agent audit logs, vendor agreements), and notes that legal or auditor review is needed. FAIL if it only explains what ISO 42001 is."),
],
"adlc-operate": [
 ("agent-traces", "agentops-observability",
  "Our CI agent did something weird last night and we have no idea what it actually ran. What should we capture going forward?",
  "PASS if the response specifies traces of steps and tool calls with redaction of secrets and PII at capture time, cost and latency per run, safety signals such as blocked actions, alerts for loops or anomalies, and retention and access control for traces. FAIL if it only suggests turning on verbose logging."),
],
"adlc-agent-engineering": [
 ("tool-misuse", "tool-design",
  "Our agent has tools called get_data, update_record, and query. It keeps calling the wrong one and passing bad parameters. How should we redesign them?",
  "PASS if the response recommends task-shaped tools with descriptive names and descriptions saying when to use them, typed explicit parameters, error messages that suggest the fix, concise responses, and separation of read and write tools with explicit side effects. FAIL if it only suggests adding more instructions to the system prompt."),
 ("prompt-change-broke", "prompt-versioning",
  "Someone edited our production system prompt in the vendor dashboard and the agent started giving refunds it shouldn't. How do we prevent this?",
  "PASS if the response recommends storing prompts and model settings as versioned files in the repo, reviewing changes in pull requests with eval results before and after, pinning model versions, staged rollout, logging the prompt version per run, and rollback via configuration. FAIL if it only suggests restricting dashboard access."),
],
}
for k, v in EXTRA.items():
    CASES[k].extend(v)


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    total = 0
    for plugin, cases in CASES.items():
        ev = ROOT / plugin / "evals"
        if ev.exists():
            for d in ev.iterdir():
                if d.is_dir() and d.name != "results":
                    shutil.rmtree(d)
        skills = sorted(p.parent.name for p in (ROOT / plugin).glob("skills/*/SKILL.md"))
        for name, skill, prompt, rubric in cases:
            assert skill in skills, (plugin, skill)
            c = ev / name
            write(c / "prompt.md", f"---\nmax_turns: 8\nallowed_tools: [Read, Glob, Grep, Skill]\ntags: [smoke, trigger, {skill}]\ndescription: Should invoke {skill} and apply its method\n---\n\n{prompt}\n")
            write(c / "graders" / "skill-fired.md", f"---\ntype: tool_used\ntool: Skill\ninput_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'\n---\n")
            write(c / "graders" / "method.md", f"---\ntype: llm\nweight: 2\n---\n\n{rubric}\n")
            total += 1
        alt = "|".join(skills)
        c = ev / "unrelated-request"
        write(c / "prompt.md", f"---\nmax_turns: 4\nallowed_tools: [Read, Glob, Grep, Skill]\ntags: [smoke, negative]\ndescription: Must not invoke any {plugin} skill\n---\n\n{NEGATIVE[plugin]}\n")
        write(c / "graders" / "no-plugin-skill.md", f"---\ntype: tool_used\ntool: Skill\ninput_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?({alt})\"'\nmin: 0\nmax: 0\narm: both\n---\n")
        write(c / "graders" / "answered.md", "---\ntype: llm\n---\n\nPASS if the response directly and correctly answers the question without introducing unrelated process, frameworks, or engineering methodology.\nFAIL if it is wrong or drags in unrelated methodology.\n")
        total += 1
    print(f"Wrote {total} eval cases across {len(CASES)} plugins")


if __name__ == "__main__":
    main()
