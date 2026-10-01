#!/usr/bin/env python3
"""Source of truth for which market standards each skill is grounded in.
Inserts a '**Grounded in:**' line under each skill's H1 and merges the sources into '### Further Reading'.
Run: python3 scripts/grounding.py
"""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent

S = {
 "dora": ("DORA research (State of AI-assisted Software Development, AI Capabilities Model)", "https://dora.dev/research/publications/"),
 "dx": ("DX AI Measurement Framework", "https://getdx.com/blog/ai-measurement-framework-guide/"),
 "metr": ("METR: early-2025 AI and experienced OS developer productivity (RCT)", "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/"),
 "trends": ("Anthropic: 2026 Agentic Coding Trends Report", "https://resources.anthropic.com/2026-agentic-coding-trends-report"),
 "radar": ("Thoughtworks Technology Radar (Vol. 34, April 2026)", "https://www.thoughtworks.com/radar"),
 "knight": ("Feng, McDonald, Zhang: Levels of Autonomy for AI Agents (Knight First Amendment Institute)", "https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1"),
 "owasp_agentic": ("OWASP Top 10 for Agentic Applications (2026)", "https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/"),
 "nist_rmf": ("NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework"),
 "nist_600": ("NIST AI 600-1: Generative AI Profile", "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf"),
 "ssdf": ("NIST SP 800-218A: SSDF Community Profile for Generative AI", "https://csrc.nist.gov/pubs/sp/800/218/a/final"),
 "zerotrust": ("NIST SP 800-207: Zero Trust Architecture", "https://csrc.nist.gov/pubs/sp/800/207/final"),
 "iso42001": ("ISO/IEC 42001 AI management system", "https://www.iso.org/standard/81230.html"),
 "euaiact": ("EU AI Act resource site", "https://artificialintelligenceact.eu/"),
 "openssf": ("OpenSSF: Security-Focused Guide for AI Code Assistant Instructions", "https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions"),
 "mcp_sec": ("Model Context Protocol: Security best practices", "https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices"),
 "snyk": ("Snyk: ToxicSkills study of the agent-skills supply chain", "https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/"),
 "pkg_hallu": ("Spracklen et al.: package hallucinations by code-generating LLMs", "https://arxiv.org/abs/2406.10279"),
 "g_review": ("Google Engineering Practices: code review guide", "https://google.github.io/eng-practices/review/"),
 "g_small": ("Google Engineering Practices: small CLs", "https://google.github.io/eng-practices/review/developer/small-cls.html"),
 "g_desc": ("Google Engineering Practices: writing good CL descriptions", "https://google.github.io/eng-practices/review/developer/cl-descriptions.html"),
 "codeowners": ("GitHub Docs: About code owners", "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners"),
 "linearb": ("LinearB: 2026 AI in software development benchmarks", "https://linearb.io/library/ai-in-software-development"),
 "sre_pm": ("Google SRE Book: Postmortem culture", "https://sre.google/sre-book/postmortem-culture/"),
 "etsy": ("Etsy Code as Craft: Blameless postmortems and a just culture", "https://www.etsy.com/codeascraft/blameless-postmortems"),
 "sre_risk": ("Google SRE Book: Embracing risk (error budgets)", "https://sre.google/sre-book/embracing-risk/"),
 "toggles": ("Martin Fowler: Feature toggles", "https://martinfowler.com/articles/feature-toggles.html"),
 "tbd": ("Trunk-based development", "https://trunkbaseddevelopment.com/"),
 "strangler": ("Martin Fowler: Strangler fig application", "https://martinfowler.com/bliki/StranglerFigApplication.html"),
 "c4": ("The C4 model for software architecture", "https://c4model.com/"),
 "madr": ("MADR: Markdown Architectural Decision Records", "https://adr.github.io/madr/"),
 "archunit": ("ArchUnit: architecture tests", "https://www.archunit.org/"),
 "speckit": ("GitHub Spec Kit", "https://github.com/github/spec-kit"),
 "aidlc": ("AWS AI-DLC workflows", "https://github.com/awslabs/aidlc-workflows"),
 "ears": ("EARS: Easy Approach to Requirements Syntax", "https://alistairmavin.com/ears/"),
 "gherkin": ("Cucumber: Gherkin reference", "https://cucumber.io/docs/gherkin/reference/"),
 "invest": ("Bill Wake: INVEST in good stories and SMART tasks", "https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/"),
 "pact": ("Pact: consumer-driven contract testing", "https://docs.pact.io/"),
 "hypothesis": ("Hypothesis: property-based testing", "https://hypothesis.works/"),
 "stryker": ("Stryker: mutation testing", "https://stryker-mutator.io/"),
 "scrum_dod": ("The Scrum Guide (Definition of Done)", "https://scrumguides.org/scrum-guide.html"),
 "cc_best": ("Claude Code best practices", "https://code.claude.com/docs/en/best-practices"),
 "cc_hooks": ("Claude Code hooks reference", "https://code.claude.com/docs/en/hooks"),
 "cc_skills": ("Claude Code: skills", "https://code.claude.com/docs/en/skills"),
 "cc_evals": ("Claude Code: test plugins with evals", "https://code.claude.com/docs/en/plugin-evals"),
 "agents_md": ("AGENTS.md open format", "https://agents.md/"),
 "ctx_eng": ("Anthropic: Effective context engineering for AI agents", "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"),
 "harness": ("OpenAI: Harness engineering", "https://openai.com/index/harness-engineering/"),
 "long_run": ("Anthropic: Harness design for long-running application development", "https://www.anthropic.com/engineering/harness-design-long-running-apps"),
 "building_agents": ("Anthropic: Building effective agents", "https://www.anthropic.com/engineering/building-effective-agents"),
 "tools": ("Anthropic: Writing effective tools for agents", "https://www.anthropic.com/engineering/writing-tools-for-agents"),
 "evals": ("Anthropic: Demystifying evals for AI agents", "https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents"),
 "twelve": ("12-Factor Agents", "https://github.com/humanlayer/12-factor-agents"),
 "otel": ("OpenTelemetry GenAI semantic conventions", "https://github.com/open-telemetry/semantic-conventions-genai"),
 "finops": ("FinOps Foundation: FinOps for AI", "https://www.finops.org/framework/technology-categories/ai/"),
 "gh_cai": ("GitHub: Continuous AI in practice", "https://github.blog/ai-and-ml/generative-ai/continuous-ai-in-practice-what-developers-can-automate-today-with-agentic-ci/"),
 "skill_form": ("Anthropic Research: How AI assistance impacts the formation of coding skills", "https://www.anthropic.com/research/AI-assistance-coding-skills"),
 "topologies": ("Team Topologies: key concepts (enabling teams)", "https://teamtopologies.com/key-concepts"),
 "skillsbench": ("SkillsBench", "https://arxiv.org/abs/2602.12670"),
 "sweskills": ("SWE-Skills-Bench", "https://arxiv.org/abs/2603.15401"),
 "superpowers": ("Superpowers", "https://github.com/obra/superpowers"),
 "official": ("Anthropic official plugin directory", "https://github.com/anthropics/claude-plugins-official"),
}

G = {
 # foundations
 "adlc-readiness-assessment": ["dora", "dx", "radar"],
 "sdlc-to-adlc-mapping": ["aidlc", "trends", "radar"],
 "autonomy-levels": ["knight", "owasp_agentic", "trends"],
 "ai-stance-policy": ["dora", "iso42001", "nist_rmf"],
 "adlc-metrics": ["dora", "dx", "metr"],
 "ai-champions-program": ["topologies", "dora"],
 "role-transitions": ["trends", "skill_form"],
 "comprehension-debt": ["skill_form", "radar"],
 # intent
 "agentic-prd": ["speckit", "radar", "cc_best"],
 "spec-driven-development": ["speckit", "aidlc", "radar"],
 "acceptance-criteria": ["ears", "gherkin"],
 "spec-clarification": ["speckit", "radar"],
 "task-decomposition": ["invest", "speckit"],
 "architecture-guardrails": ["madr", "archunit", "harness", "radar"],
 # context
 "agent-context-files": ["agents_md", "openssf", "harness", "cc_best"],
 "codebase-map": ["c4", "harness"],
 "context-budget": ["ctx_eng", "cc_best"],
 "codify-conventions": ["radar", "cc_skills", "cc_hooks"],
 "mcp-integration-plan": ["mcp_sec", "owasp_agentic", "dora"],
 "skill-library-management": ["skillsbench", "sweskills", "cc_evals", "radar"],
 # build
 "execution-rail-selection": ["radar", "superpowers", "speckit", "official"],
 "long-running-agent-work": ["long_run", "trends"],
 "small-batch-delivery": ["g_small", "tbd", "toggles", "dora"],
 "legacy-modernization": ["strangler", "official"],
 # verify
 "review-capacity": ["g_review", "codeowners", "linearb", "radar"],
 "behavioral-testing": ["hypothesis", "pact", "stryker", "radar"],
 "tests-from-specs": ["gherkin", "speckit"],
 "agent-code-review": ["g_review", "openssf", "radar"],
 "hallucination-checks": ["pkg_hallu", "openssf", "ssdf"],
 "definition-of-done": ["scrum_dod", "openssf", "cc_best"],
 # govern
 "agentic-threat-model": ["owasp_agentic", "nist_600", "mcp_sec"],
 "agent-permissions": ["zerotrust", "owasp_agentic", "cc_best"],
 "guardrail-hooks": ["cc_hooks", "openssf"],
 "ai-compliance-mapping": ["iso42001", "nist_rmf", "euaiact", "ssdf"],
 "extension-vetting": ["owasp_agentic", "snyk", "mcp_sec"],
 "citizen-builder-governance": ["trends", "radar", "nist_rmf"],
 # operate
 "release-gates": ["sre_risk", "toggles", "dora"],
 "agentops-observability": ["otel", "owasp_agentic"],
 "ai-cost-management": ["finops", "dx"],
 "agent-incident-review": ["sre_pm", "etsy", "owasp_agentic"],
 "continuous-ai-workflows": ["gh_cai", "harness", "owasp_agentic"],
 "learning-loop": ["sre_pm", "radar", "harness"],
 # agent engineering
 "agent-architecture": ["building_agents", "twelve", "knight"],
 "tool-design": ["tools", "mcp_sec"],
 "eval-suite-design": ["evals", "nist_rmf"],
 "prompt-versioning": ["twelve", "evals"],
 "agent-runtime-guardrails": ["owasp_agentic", "knight", "nist_600"],
}

def apply():
    missing = []
    for f in sorted(ROOT.glob("adlc-*/skills/*/SKILL.md")):
        name = f.parent.name
        if name not in G:
            missing.append(name); continue
        keys = G[name]
        t = f.read_text(encoding="utf-8")
        names = "; ".join(S[k][0] for k in keys)
        line = f"**Grounded in:** {names}."
        t = re.sub(r"\n\*\*Grounded in:\*\*[^\n]*\n", "\n", t)
        t = re.sub(r"(^# [^\n]+\n)", r"\1\n" + line.replace("\\", "\\\\") + "\n", t, count=1, flags=re.M)
        if "### Further Reading" not in t:
            t = t.rstrip() + "\n\n---\n\n### Further Reading\n"
        head, fr = t.split("### Further Reading", 1)
        existing = set(re.findall(r"\]\((https?://[^)]+)\)", fr))
        add = [f"- [{S[k][0]}]({S[k][1]})" for k in keys if S[k][1] not in existing]
        fr = fr.rstrip() + ("\n" if fr.strip() else "\n") + "\n".join(add) + "\n"
        t = (head + "### Further Reading" + re.sub(r"\n{3,}", "\n\n", fr)).rstrip() + "\n"
        f.write_text(t, encoding="utf-8")
    return missing

if __name__ == "__main__":
    m = apply()
    print("missing mapping:", m)

def write_map():
    from collections import defaultdict
    by_std = defaultdict(list)
    for skill, keys in G.items():
        for k in keys: by_std[k].append(skill)
    lines = ["# Standards Map", "",
             "Every skill in ADLC Skills applies recognized market practice. This map is generated from `scripts/grounding.py`; the validator fails any skill without a **Grounded in** line and at least two primary sources.", "",
             "## By skill", "", "| Plugin | Skill | Grounded in |", "|--------|-------|-------------|"]
    for f in sorted(ROOT.glob("adlc-*/skills/*/SKILL.md")):
        n = f.parent.name
        lines.append(f"| {f.parent.parent.parent.name} | `{n}` | " + "; ".join(f"[{S[k][0]}]({S[k][1]})" for k in G[n]) + " |")
    lines += ["", "## By standard", "", "| Standard | Used by |", "|----------|---------|"]
    for k in sorted(by_std, key=lambda k: (-len(by_std[k]), S[k][0])):
        lines.append(f"| [{S[k][0]}]({S[k][1]}) | " + ", ".join(f"`{s}`" for s in sorted(by_std[k])) + " |")
    lines += ["", "## What is this kit's own synthesis", "",
              "Where no market standard exists, the kit says so in the skill itself: the five-level ADLC maturity scale (organized around DORA capabilities), the four-factor autonomy scoring heuristic (layered on the published Levels of Autonomy), PR-size and review-tier defaults (operationalizing Google's small-CL and review guidance), and the eval rubrics. Treat these as calibratable defaults.", ""]
    (ROOT / "docs" / "STANDARDS-MAP.md").write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    write_map()
