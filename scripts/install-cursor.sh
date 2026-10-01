#!/usr/bin/env bash
# Install ADLC Skills plugins into Cursor as local plugins (~/.cursor/plugins/local).
# Usage:  bash scripts/install-cursor.sh adlc-foundations adlc-verify     (or: all)
# Then in Cursor: Developer: Reload Window, and check Customize for the plugin.
# Re-run after `git pull` to update. Cursor skips symlinks to folders outside its plugin
# directory, so plugins are copied, not linked.
set -euo pipefail
cd "$(dirname "$0")/.."
DEST="${CURSOR_PLUGINS_DIR:-$HOME/.cursor/plugins/local}"
ALL=$(ls -d adlc-*/ | tr -d /)

if [ $# -eq 0 ]; then
  echo "Usage: bash scripts/install-cursor.sh <plugin> [plugin...] | all"
  echo "Plugins: $ALL" | tr '\n' ' '; echo; exit 1
fi
[ "$1" = "all" ] && set -- $ALL

mkdir -p "$DEST"
for p in "$@"; do
  if [ ! -f "$p/.cursor-plugin/plugin.json" ]; then echo "Unknown plugin: $p"; exit 1; fi
  rm -rf "${DEST:?}/$p"
  mkdir -p "$DEST/$p"
  # Copy what Cursor uses; leave out Codex-only workflows and Claude Code evals.
  cp -R "$p/.cursor-plugin" "$p/skills" "$p/README.md" "$DEST/$p/"
  [ -d "$p/commands" ] && cp -R "$p/commands" "$DEST/$p/"
  [ -d "$p/agents" ] && cp -R "$p/agents" "$DEST/$p/"
  echo "Installed $p -> $DEST/$p"
done
echo "Now run 'Developer: Reload Window' in Cursor, then open Customize to confirm."
