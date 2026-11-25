# Contributing

## Layout

| Path | What |
|---|---|
| `plugins/gptunnel/` | Main plugin: full MCP `https://gptunnel.ru/mcp`, all skills. Listed in our marketplaces for Claude Code, Codex and Cursor. |
| `plugins/gptunnel-claude/` | Anthropic plugin directory variant: MCP `https://gptunnel.ru/mcp/claude` (media library only: find, export, organize existing media; no workflows, no paid calls — directory policy 4(B) and the "drafts generation jobs" check). Not listed in our marketplaces. |
| `tools/full.txt`, `tools/catalog.txt` | Tool names of each MCP surface. Skills may name only these tools. |
| `scripts/check.py` | Static checks, run in CI. |
| `evals/<plugin>/` | Behavior evals with a mocked MCP server, run with `scripts/eval.sh <plugin>`. Kept outside the plugin folders: the Anthropic directory rejects eval files inside a submitted plugin. |

## Skill rules

- Only skills useful to GPTunneL users. No developer docs (API examples, error codes, model reference).
- `name` equals the folder name. The description says what the skill does, then `Use when …`, then `NOT for … (use <skill>)`. Up to 1024 characters.
- No prices in skills: take them from `lab_quote` / `apps_list` at run time. Models are recommendations by property; the agent confirms them with `lab_list_models` / `lab_get_model`.
- Every paid call: show the price first, pass `max_cost_rub`, a fresh `request_id`. Never retry a paid call silently.
- The catalog variant must not name paid tools, offer image/video generation or draft generation jobs (workflows, templates, prompts to render): Anthropic directory policy 4(B).

## Release

1. Change `VERSION` and the same version in every manifest (`scripts/check.py` checks they match).
2. `python3 scripts/check.py` and `claude plugin validate .`.
3. Install from a local path in a temporary profile: `CLAUDE_CONFIG_DIR=$(mktemp -d) claude plugin marketplace add "$PWD"`, Codex `CODEX_HOME=$(mktemp -d) codex plugin marketplace add "$PWD"`, Cursor `cursor-agent --plugin-dir plugins/gptunnel`.
4. Run evals before changing skill behavior: `scripts/eval.sh gptunnel --runs 1` (see `evals/<plugin>/README.md`).

When the MCP server adds or removes tools, update `tools/*.txt` in the same change.
