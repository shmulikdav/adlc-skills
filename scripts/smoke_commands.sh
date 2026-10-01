#!/usr/bin/env bash
# Smoke test: run every plugin command headlessly, exactly as the docs write it,
# and flag commands that fail to resolve, error out, or produce no answer.
# Usage:  bash scripts/smoke_commands.sh [model]     (default model: sonnet)
# Output: smoke-results/<plugin>__<command>.txt plus a summary table. Read a few outputs yourself.
set -uo pipefail
cd "$(dirname "$0")/.."
MODEL="${1:-sonnet}"
OUT="smoke-results"; rm -rf "$OUT"; mkdir -p "$OUT"
CONTEXT="Context: 40-engineer B2B SaaS company, TypeScript and Python, GitHub, Claude Code for all engineers for two months, weekly deploys, about 35% test coverage, no written AI policy, agent PRs wait 3 days for review. Make reasonable assumptions instead of asking questions."

PLUGIN_ARGS=()
for p in adlc-*/; do PLUGIN_ARGS+=(--plugin-dir "${p%/}"); done

fail_pattern='Unknown (slash )?command|Unknown skill|command not found|is not a valid|isn.t available|No such command|Error:'

run() {  # $1 = slash command text, $2 = output file; writes answer to $2 and skill-load count to $2.skills
  claude -p "$1 $CONTEXT" "${PLUGIN_ARGS[@]}" --model "$MODEL" --max-turns 10 \
    --allowedTools "Read Glob Grep Skill" --output-format stream-json --verbose < /dev/null > "$2.jsonl" 2>&1
  if grep -qi "Not logged in\|Login expired" "$2.jsonl"; then echo "Not logged in: run claude, then /login, then re-run this script."; exit 1; fi
  python3 - "$2" <<'EOF'
import json, sys
out = sys.argv[1]; text = ""; skills = 0
for line in open(out + ".jsonl", errors="ignore"):
    try: ev = json.loads(line)
    except ValueError: continue
    if ev.get("type") == "assistant":
        for block in ev.get("message", {}).get("content", []):
            if block.get("type") == "tool_use" and block.get("name") == "Skill": skills += 1
    if ev.get("type") == "result": text = ev.get("result") or ""
open(out, "w").write(text); open(out + ".skills", "w").write(str(skills))
EOF
}

printf "%-24s %-24s %-7s %-7s %s\n" PLUGIN COMMAND RESULT SKILLS "WORKS AS"
pass=0; warn=0; fail=0
for p in adlc-*/; do
  p=${p%/}
  for f in "$p"/commands/*.md; do
    c=$(basename "$f" .md); o="$OUT/${p}__${c}.txt"
    run "/$c" "$o"
    if [ -s "$o" ] && ! grep -Eqi "$fail_pattern" "$o" && [ "$(wc -w < "$o")" -gt 60 ]; then
      res=PASS; how="/$c"
    else
      run "/$p:$c" "$o"
      if [ -s "$o" ] && ! grep -Eqi "$fail_pattern" "$o" && [ "$(wc -w < "$o")" -gt 60 ]; then
        res=PASS; how="/$p:$c  (short form failed)"
      else
        res=FAIL; how="see $o"
      fi
    fi
    sk=$(cat "$o.skills" 2>/dev/null || echo 0)
    if [ "$res" = PASS ] && [ "$sk" -eq 0 ]; then res=WARN; how="$how  (no skill loaded)"; fi
    case $res in PASS) pass=$((pass+1));; WARN) warn=$((warn+1));; *) fail=$((fail+1));; esac
    printf "%-24s %-24s %-7s %-7s %s\n" "$p" "$c" "$res" "$sk" "$how"
  done
done
echo; echo "$pass passed, $warn ran without loading a skill, $fail failed. Answers in $OUT/*.txt — open a few and read them."
