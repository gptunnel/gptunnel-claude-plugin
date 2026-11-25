---
name: gptunnel-setup
description: Connect the agent to the user's GPTunneL account and check that it works — sign-in, which account and organizations are connected, what to try first. Use when the user installs the GPTunneL plugin, asks to connect or log in to GPTunneL, or when GPTunneL tools are missing or return an authorization error. NOT for generating anything (use lab-generate or a scenario skill such as marketplace-cards).
---

# Connect GPTunneL

The plugin connects to the GPTunneL MCP server `https://gptunnel.ru/mcp`. Sign-in is OAuth in the browser: there is no API key to paste, and you never ask the user for a password.

## 1. Check the connection

Call `whoami`.

- **It returns a user id and scopes** — connected. Go to step 3.
- **GPTunneL tools are not available, or the server answers 401 / "needs authentication"** — the user has not signed in yet. Go to step 2.
- **403 "MCP access is not enabled for this account"** — the account is signed in, but MCP is not enabled for it yet. Tell the user to write to support@gptunnel.ai; signing in again will not help.
- **Error about a blocked or deleted account** — say so plainly and point to support@gptunnel.ai.

## 2. Sign in

The user completes the browser step themselves. Tell them exactly what to do in their client:

| Client | What the user does |
|---|---|
| Claude Code | Run `/mcp`, choose `gptunnel`, press Authenticate, sign in on gptunnel.ru and allow access |
| Codex | Run `codex mcp login gptunnel` in the terminal, sign in in the browser |
| Cursor | Settings → MCP → `gptunnel` → Connect, sign in in the browser |

On the consent screen GPTunneL lists what the agent may do (read and edit workflows, generate in the Lab, manage the gallery). The user can untick spending scopes: then the agent can browse and build, but not generate.

After the user confirms, call `whoami` again.

## 3. Show what is connected

- `whoami` — the account and granted scopes. If `lab:generate` is missing, generation is off for this connection: say so before the user asks for an image.
- `list_orgs` — personal account and organizations. If there are organizations, ask which balance should pay by default and remember the `org_id` for this conversation.

## 4. Suggest a first task

Offer three short options in the user's language, for example:

- "Make Wildberries cards from a product photo" (marketplace-cards)
- "Generate an image — I will show the price first" (lab-generate)
- "Remove the background from a photo" (photo-retouch)

Keep it short: no internals, no tool names in the reply to the user.
