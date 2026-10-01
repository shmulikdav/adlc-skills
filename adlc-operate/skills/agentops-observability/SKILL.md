---
name: agentops-observability
description: "Instrument agents and agentic workflows for observability: traces of steps and tool calls, inputs/outputs with redaction, latency, token usage, error and retry rates, human intervention points, and dashboards and alerts. Use when running agents in CI or production, debugging agent behavior after the fact, building an AgentOps practice, or needing an audit trail of what an agent did."
---

# AgentOps Observability

## Purpose

When an agent misbehaves, the transcript is the evidence. Without traces you can't debug, audit, or improve. Observability is also the raw material for evals and for cost control.

## What to capture

| Signal | Detail |
|--------|--------|
| Trace | Session/run ID, step sequence, tool calls with arguments (redacted), results summary, decisions |
| Inputs/outputs | Prompts, context sources used (by reference), final outputs; PII and secrets redacted at capture time |
| Performance | Latency per step and end to end; retries; timeouts |
| Cost | Input/output/cached tokens per step, model used, cost per run and per outcome |
| Quality | Task success (outcome check), human overrides, rework, eval scores |
| Safety | Blocked actions (hooks/permissions), injection detections, escalations to humans |

## Instructions

1. Identify the agent runs to instrument (interactive coding, CI agents, production agent features).
2. Choose capture points and a trace schema; prefer an OpenTelemetry-compatible format so traces join existing observability.
3. Define redaction rules before turning capture on.
4. Build three views: **operations** (errors, latency, volume), **quality** (success, overrides, rework), **economics** (cost per outcome).
5. Set alerts on: error spikes, cost anomalies per run, loops (step count above threshold), repeated blocked actions.
6. Define retention and access control for traces (they may contain sensitive data).

## Output

Trace schema, redaction policy, dashboard spec (panels and queries described), alert rules, retention policy.
