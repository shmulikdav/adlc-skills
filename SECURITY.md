# Security Policy

## What this repository contains

ADLC Skills is mostly instructions (Markdown skills, commands, and agent definitions). Installing a plugin does **not** activate any executable code: there are no plugin hooks, MCP servers, or binaries in the plugins. Two scripts are meant to run in your environment, both opt-in: the hook template under `templates/hooks/`, which you copy and wire up yourself, and `scripts/install-cursor.sh`, which copies plugin folders into `~/.cursor/plugins/local` for Cursor users (read it before running; it only copies files). The other files in `scripts/` are maintainer tools for regenerating manifests and running tests.

Still, skills shape what an agent does, so we treat malicious or unsafe instructions as security issues.

## Reporting a vulnerability

Please **do not open a public issue** for security problems. Report privately through GitHub's **Report a vulnerability** button on the Security tab, or email shmulik@braightwave.com with "ADLC Skills security" in the subject.

Include the file and line, what an agent could be led to do, and a reproduction prompt if you have one. You can expect an acknowledgement within 5 business days.

## In scope

- Instructions that could lead an agent to exfiltrate data, weaken security controls, or execute untrusted code
- Prompt-injection vectors in skills, commands, agents, or eval fixtures
- Problems in the hook template or CI workflows (for example, secrets exposure)

## Before you install any third-party skills

Including these. Read them first; the `adlc-govern:extension-vetting` skill gives you a checklist.
