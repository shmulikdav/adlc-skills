---
name: citizen-builder-policy
description: "Run the ADLC citizen-builder-policy workflow: create a paved-road policy for non-engineers building tools and apps with AI — tiers, data rules, inventory, promotion to engineering. Use when the user invokes $citizen-builder-policy or asks for this workflow end to end."
---

> Generated from the Claude Code command `/citizen-builder-policy` by scripts/sync_cross_platform.py. Do not edit; edit the command instead.

# $citizen-builder-policy -- Business-Team Builder Governance

## Invocation

```
$citizen-builder-policy Finance and ops teams are building automations in Cowork and Lovable on our ERP data
```

## Workflow

Input: the user's request

### Step 0: Load the method
Before anything else, open and read each of these skills from this plugin's skill list: `adlc-govern:citizen-builder-governance`, `adlc-govern:extension-vetting`. This workflow is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Inventory and tier
Apply the **citizen-builder-governance** skill to classify existing tools into tiers.

### Step 2: Paved road
Approved tools and connectors, data rules, templates, promotion triggers, and the review process.

### Step 3: Extensions
Apply **extension-vetting** to the plugins, skills, and connectors business teams want to use.

### Step 4: Output
Policy document, inventory template, and a one-paragraph announcement for business teams.

### Finally: suggest the next step
End with one short line suggesting at most two of these, chosen by what you found:
- `$governance-pack`: align it with the engineering policy
- `$threat-model`: for apps that touch customer data
