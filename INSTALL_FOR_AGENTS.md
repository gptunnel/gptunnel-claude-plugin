# Install for agents

You are an AI agent. The user asked you to install the GPTunneL plugin. Follow these steps exactly.

The plugin is a GPTunneL MCP server connection (`https://gptunnel.ru/mcp`) plus skills. There is nothing to compile and no API key: the user signs in to GPTunneL in the browser (OAuth).

## Step 1 — Install for your host

**Claude Code** — run, then ask the user to restart Claude Code:

```bash
claude plugin marketplace add gptunnel/gptunnel-claude-plugin
claude plugin install gptunnel@gptunnel
```

**Codex** — run, then ask the user to restart Codex:

```bash
codex plugin marketplace add gptunnel/gptunnel-claude-plugin
codex plugin add gptunnel@gptunnel
```

**Cursor** — add the marketplace with the Cursor CLI, then ask the user to install **GPTunneL** in Cursor → Settings → Plugins and reload Cursor:

```bash
agent plugin marketplace add https://github.com/gptunnel/gptunnel-claude-plugin
```

If the `agent` CLI is not installed, ask the user to add the marketplace URL in Cursor → Settings → Plugins themselves.

**Another agent without plugins** — add only the MCP server: an HTTP (streamable) server named `gptunnel` with URL `https://gptunnel.ru/mcp`. Skills from `plugins/gptunnel/skills/` can be copied into the agent's skills folder if it supports Agent Skills.

## Step 2 — Sign in

Ask the user to sign in; you cannot do this step for them and must never ask for their password.

| Host | What the user does |
|---|---|
| Claude Code | `/mcp` → `gptunnel` → Authenticate |
| Codex | `codex mcp login gptunnel` |
| Cursor | Settings → MCP → `gptunnel` → Connect |

Wait until the user confirms.

## Step 3 — Verify

Call the `whoami` tool. Expect a user id and a list of scopes.

- 401 or "needs authentication" → repeat Step 2.
- 403 "MCP access is not enabled for this account" → the account has no MCP access yet; the user writes to support@gptunnel.ai.
- Tool not found → the host was not restarted after Step 1.

Do not run a generation to test the install: generations are paid.

## Step 4 — Done

Tell the user: "GPTunneL is connected. Try: make marketplace cards from a product photo, generate an image (I will show the price first), or remove a photo background."

Do not explain the internals (paths, manifests, tool names).
