#!/usr/bin/env bash
# PreToolUse guardrail: block agent edits to protected paths.
# Wire it from .claude/settings.json (see templates/hooks/settings.example.json).
# Reads the hook payload (JSON) on stdin; exits 2 to block with a reason on stderr.
# Verify the hook contract against the current Claude Code hooks documentation before use.
set -euo pipefail

payload="$(cat)"
file_path="$(printf '%s' "$payload" | python3 -c 'import json,sys; d=json.load(sys.stdin); print((d.get("tool_input") or {}).get("file_path",""))')"

[ -z "$file_path" ] && exit 0

protected_patterns=(
  '(^|/)\.env($|\.)'
  '(^|/)secrets?/'
  '\.pem$'
  '\.key$'
  '(^|/)\.github/workflows/'
  '(^|/)migrations/applied/'
  '(^|/)(package-lock\.json|pnpm-lock\.yaml|yarn\.lock|poetry\.lock)$'
)

for pattern in "${protected_patterns[@]}"; do
  if printf '%s' "$file_path" | grep -Eq "$pattern"; then
    echo "Blocked by guardrail: '$file_path' is a protected path. Ask a human to make this change or explain why it is needed." >&2
    exit 2
  fi
done

exit 0
