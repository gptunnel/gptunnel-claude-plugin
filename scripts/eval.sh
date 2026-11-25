#!/usr/bin/env bash
# Run the eval suite of one plugin: scripts/eval.sh <gptunnel|gptunnel-claude> [extra claude plugin eval flags]
# Evals live outside the plugin folders: the Anthropic directory rejects eval files inside a submitted plugin.
set -euo pipefail
plugin="${1:?plugin name}"; shift
root="$(cd "$(dirname "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
cp -R "$root/plugins/$plugin" "$tmp/$plugin"
cp -R "$root/evals/$plugin" "$tmp/$plugin/evals"
out="$root/evals/results/$plugin/$(date -u +%Y-%m-%dT%H-%M-%SZ)"
mkdir -p "$out"
cd "$tmp/$plugin"
claude plugin eval . --ablation none --trust-plugin --no-publish \
  --output-dir "$out" --report "$out/report.html" --json "$out/result.json" "$@"
