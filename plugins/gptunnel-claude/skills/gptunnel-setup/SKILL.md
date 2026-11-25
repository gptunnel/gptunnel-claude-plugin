---
name: gptunnel-setup
description: Connect Claude to the user's GPTunneL account and check that it works — sign-in, which account and organizations are connected, what to try first. Use when the user installs the GPTunneL plugin, asks to connect or log in to GPTunneL, or when GPTunneL tools are missing or return an authorization error. NOT for working with workflows or the media library themselves (use workflow-build, workflow-templates or gallery-organize).
---

# Connect GPTunneL

The plugin connects to the GPTunneL MCP server `https://gptunnel.ru/mcp/claude`. Sign-in is OAuth in the browser: there is no API key to paste, and you never ask the user for a password.

## 1. Check the connection

Call `whoami`.

- **It returns a user id and scopes** — connected. Go to step 3.
- **GPTunneL tools are not available, or the server answers 401 / "needs authentication"** — the user has not signed in. In Claude Code: run `/mcp`, choose `gptunnel`, press Authenticate, sign in on gptunnel.ru and allow access. In Claude apps: Settings → Connectors → GPTunneL → Connect. Then call `whoami` again.
- **403 "MCP access is not enabled for this account"** — the account is signed in, but MCP is not enabled for it yet. Tell the user to write to support@gptunnel.ai; signing in again will not help.
- **Error about a blocked or deleted account** — say so plainly and point to support@gptunnel.ai.

## 2. What the connection allows

This connection reads and edits the user's workflows and media library. It does not run workflows and does not spend the balance: running happens in the GPTunneL editor on gptunnel.ru, where the user sees the cost.

## 3. Show what is connected

- `whoami` — the account and granted scopes.
- `list_orgs` — personal account and organizations. If there are organizations, ask which one to work in and remember its `org_id` for this conversation.

## 4. Suggest a first task

Offer three short options in the user's language, for example:

- "Find a ready workflow template for my task and copy it to my account" (workflow-templates)
- "Explain what my workflow does and check it for mistakes" (workflow-review)
- "Sort my recent results into collections" (gallery-organize)

Keep it short: no internals, no tool names in the reply to the user.
