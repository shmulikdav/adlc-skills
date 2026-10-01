# ADLC Research Notes

Research behind ADLC Skills, compiled October 2026. Summaries are paraphrased; follow the links for the primary sources.

## 1. What "ADLC" means

The acronym is used in two distinct senses. Being explicit about which one you mean avoids confusion with clients and in workshops.

| Sense | Meaning | Who uses it this way | Where it lives in this repo |
|-------|---------|----------------------|------------------------------|
| **Agentic** development lifecycle | The software delivery lifecycle executed largely by AI agents, with humans setting intent, boundaries, and gates | Security vendors (Cycode, OX Security), consultancies (Palo IT, SumatoSoft), most practitioner writing | Plugins 0–6 |
| **Agent** development lifecycle | The lifecycle for building and operating AI agents as products (evals, guardrails, AgentOps) | IBM, Microsoft, Cognizant, EPAM's AI/Run | `adlc-agent-engineering` |

Related terms:

- **AI-DLC** (AWS): AI-Driven Development Lifecycle. Three phases — Inception, Construction, Operations — with human validation of every AI-proposed plan and short work cycles AWS calls "bolts". Open-sourced as markdown workflow rules that run in Kiro, Claude Code, Cursor, Copilot, and others.
- **AI-SDLC / AI-assisted SDLC**: humans remain the executors and AI assists. Most sources draw the line here: assistance is not ADLC; delegation of multi-step execution is.
- **Spec-Driven Development (SDD)**: the specification is the durable source of truth that agents implement against (GitHub Spec Kit, Kiro specs). Widely described as the core practice of the ADLC.

### Phase models compared

| Source | Phases |
|--------|--------|
| Cycode | Requirements & guardrails → architecture planning → code generation → testing → review & deployment → monitoring |
| Talentica | Ideation & intent specification → architecture & scaffolding → development & inner loop → behavioral testing & validation → deployment & orchestration → governance & continuous learning |
| SumatoSoft | Hypothesis & guardrails → intent & scope → agentic architecture → simulation & proof of value → implementation & continuous evaluation → red-teaming → activation & AgentOps |
| AWS AI-DLC | Inception → Construction → Operations |
| GitHub Spec Kit | Constitution → specify → clarify → plan → tasks → implement → converge |
| **This repo** | Foundations → Intent → Context → Build → Verify → Govern (cross-cutting) → Operate, plus Agent Engineering |

The common thread: the stages stay recognizable; the executor changes, the artifacts shift toward machine-readable specs and context, and the human role concentrates on intent and verification. This repo adds an explicit **Context** phase because context engineering is where most practical agent failures originate, and an explicit **Foundations** phase because the research says organizational capabilities decide outcomes.

## 2. Evidence on outcomes

**DORA 2025 — State of AI-assisted Software Development.** Based on nearly 5,000 technology professionals. Central finding: AI is an amplifier — it magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones. AI improved throughput in 2025, often at the cost of stability where foundations are weak.

**DORA AI Capabilities Model (Dec 2025).** Seven capabilities that amplify AI's positive impact: clear and communicated AI stance; healthy data ecosystem; AI-accessible internal data; strong version control practices; working in small batches; user-centric focus; quality internal platform. → `adlc-readiness-assessment`, `ai-stance-policy`, `mcp-integration-plan`, `small-batch-delivery`.

**METR (July 2025) randomized controlled trial.** 16 experienced open-source developers, 246 real tasks in large mature repos they knew well. With AI allowed, tasks took about 19% longer on average, while developers believed they had been sped up by roughly 20%. METR notes the setting (expert developers, complex familiar codebases, early-2025 tools) limits generalization. Lesson for the ADLC: perceived productivity is not a metric; measure with baselines and comparisons. → `adlc-metrics`.

## 3. Practice sources

**Anthropic — Claude Code best practices.** Most practices follow from one constraint: context fills fast and performance degrades as it fills. Explore → plan → implement → commit; give the agent verification criteria; keep CLAUDE.md short (bloated files get ignored); treat CLAUDE.md like code; use subagents for exploration and independent review. → `explore-plan-implement`, `agent-context-files`, `context-budget`, `agentic-tdd`.

**Anthropic — Building effective agents.** Prefer the simplest solution; workflows (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) before autonomous agents. → `agent-architecture`.

**Anthropic — Writing effective tools for agents.** Task-shaped tools, clear descriptions, token-efficient responses, helpful errors. → `tool-design`.

**Anthropic — Effective context engineering for AI agents.** Context as a finite resource; curate the smallest high-signal set. → `context-budget`, `agent-context-files`.

**Anthropic — Demystifying evals for AI agents (Jan 2026).** Vocabulary (task, trial, transcript, outcome, grader, suite); code-based, model-based, and human graders; capability vs regression evals; grade outcomes not paths; read transcripts; watch for saturation. → `eval-suite-design`.

**GitHub Spec Kit.** Constitution once per project; specify → plan → tasks → implement → converge per feature; the constitution check grounds plans in non-negotiable principles. → `spec-driven-development`.

**AWS AI-DLC workflows.** Methodology over tool; human approval required to move between phases; documentation first; runs as steering rules in many IDEs and agents. → `spec-driven-development`, `release-gates`.

## 4. Security and governance

**OWASP Top 10 for Agentic Applications (2026)**, announced December 2025 by the OWASP GenAI Security Project:

| ID | Risk |
|----|------|
| ASI01 | Agent goal hijack |
| ASI02 | Tool misuse & exploitation |
| ASI03 | Identity & privilege abuse |
| ASI04 | Agentic supply chain vulnerabilities |
| ASI05 | Unexpected code execution |
| ASI06 | Memory & context poisoning |
| ASI07 | Insecure inter-agent communication |
| ASI08 | Cascading failures |
| ASI09 | Human-agent trust exploitation |
| ASI10 | Rogue agents |

→ `agentic-threat-model`, `agent-permissions`, `guardrail-hooks`, `extension-vetting`, `agent-runtime-guardrails`.

**Frameworks for compliance mapping:** ISO/IEC 42001 (AI management system), NIST AI RMF (Govern, Map, Measure, Manage), EU AI Act (obligations by role and risk class), SOC 2 (change, access, vendor controls). → `ai-compliance-mapping`.

## 5. Packaging format

- Claude Code plugins: `.claude-plugin/plugin.json` per plugin; components (`skills/`, `commands/`, `agents/`, `hooks/`) at the plugin root; a repo becomes a marketplace with `.claude-plugin/marketplace.json`. `claude plugin validate` is the authoritative check.
- Current docs prefer `skills/` for new plugins and describe `commands/` as the older flat format; both load. This repo keeps commands as the workflow layer for parity with existing PM-skills-style marketplaces and Cowork.
- Skills follow the Agent Skills open standard (`name` + `description` frontmatter, progressive disclosure), so they work in other agents; extended frontmatter such as `allowed-tools` or `disable-model-invocation` is tool-specific.

## Sources

- Cycode — Agentic Development Lifecycle (ADLC): https://cycode.com/blog/agentic-development-lifecycle-adlc/
- OX Security — What is the ADLC: https://www.ox.security/academy/governance-compliance/what-is-the-agentic-development-lifecycle-adlc/
- EPAM — Agentic Development Lifecycle explained: https://www.epam.com/insights/ai/blogs/agentic-development-lifecycle-explained
- Cognizant — Agent development lifecycle: https://www.cognizant.com/us/en/glossary/agent-development-lifecycle
- Palo IT — What is ADLC: https://www.palo-it.com/en/blog/what-is-adlc
- Talentica — AI Development Lifecycle: https://www.talentica.com/blogs/ai-development-lifecycle/
- SumatoSoft — ADLC: https://sumatosoft.com/adlc-agentic-software-development-lifecycle
- AWS — AI-DLC workflows: https://github.com/awslabs/aidlc-workflows
- GitHub — Spec Kit: https://github.com/github/spec-kit
- DORA — publications: https://dora.dev/research/publications/
- Google Cloud — Putting the DORA AI Capabilities Model to work: https://cloud.google.com/blog/products/ai-machine-learning/from-adoption-to-impact-putting-the-dora-ai-capabilities-model-to-work/
- METR — Early-2025 AI and experienced OS developer productivity: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Anthropic — Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic — Skills: https://code.claude.com/docs/en/skills
- Anthropic — Plugin manifest reference: https://code.claude.com/docs/en/plugins-reference
- Anthropic — Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Anthropic — Writing effective tools for agents: https://www.anthropic.com/engineering/writing-tools-for-agents
- Anthropic — Effective context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic — Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- OWASP — Top 10 for Agentic Applications (2026): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001: https://www.iso.org/standard/81230.html
- EU AI Act: https://artificialintelligenceact.eu/
- Reference structure: https://github.com/phuryn/pm-skills
