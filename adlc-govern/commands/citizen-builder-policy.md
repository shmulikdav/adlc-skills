---
description: Create a paved-road policy for non-engineers building tools and apps with AI — tiers, data rules, inventory, promotion to engineering
argument-hint: "<organization context, which teams build what, tools in use>"
---

# /citizen-builder-policy -- Business-Team Builder Governance

## Invocation

```
/citizen-builder-policy Finance and ops teams are building automations in Cowork and Lovable on our ERP data
```

## Workflow

Input: $ARGUMENTS

### Step 0: Load the method
Your first action must be a Skill tool call for each of these skills: `adlc-govern:citizen-builder-governance`, `adlc-govern:extension-vetting`. This command file is only an outline: the method, rubrics, templates and defaults live in those skills, so do not answer from the outline or from general knowledge. If a skill fails to load, say so in the first line of the answer.

### Step 1: Inventory and tier
Apply the **citizen-builder-governance** skill to classify existing tools into tiers.

### Step 2: Paved road
Approved tools and connectors, data rules, templates, promotion triggers, and the review process.

### Step 3: Extensions
Apply **extension-vetting** to the plugins, skills, and connectors business teams want to use.

### Step 4: Output
Policy document, inventory template, and a one-paragraph announcement for business teams.
