#!/usr/bin/env bash
# Smoke test: run every plugin command headlessly, exactly as the docs write it,
# and flag commands that fail to resolve, error out, or produce no answer.
# Usage:  bash scripts/smoke_commands.sh [model]     (default model: sonnet)
# Output: smoke-results/<plugin>__<command>.txt plus a summary table. Read a few outputs yourself.
set -uo pipefail
cd "$(dirname "$0")/.."
MODEL="${1:-sonnet}"
OUT="smoke-results"; rm -rf "$OUT"; mkdir -p "$OUT"
CONTEXT="Context: 40-engineer B2B SaaS company, TypeScript and Python, GitHub, Claude Code for all engineers for two months, weekly deploys, about 35% test coverage, no written AI policy, agent PRs wait 3 days for review. Make reasonable assumptions instead of asking questions, and keep the answer under 400 words."

PLUGIN_ARGS=()
for p in adlc-*/; do PLUGIN_ARGS+=(--plugin-dir "${p%/}"); done

fail_pattern='Unknown (slash )?command|Unknown skill|command not found|is not a valid|isn.t available|No such command|Error:'

run() {  # $1 = slash command text, $2 = output file
  claude -p "$1 $CONTEXT" "${PLUGIN_ARGS[@]}" --model "$MODEL" --max-turns 8 \
    --allowedTools "Read Glob Grep Skill" < /dev/null > "$2" 2>&1
  if grep -qi "Not logged in\|Login expired" "$2"; then echo "Not logged in: run claude, then /login, then re-run this script."; exit 1; fi
}

printf "%-24s %-24s %-11s %s\n" PLUGIN COMMAND RESULT "WORKS AS"
pass=0; fail=0
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
    [ "$res" = PASS ] && pass=$((pass+1)) || fail=$((fail+1))
    printf "%-24s %-24s %-11s %s\n" "$p" "$c" "$res" "$how"
  done
done
echo; echo "$pass passed, $fail failed. Outputs in $OUT/ — open a few and read them."
