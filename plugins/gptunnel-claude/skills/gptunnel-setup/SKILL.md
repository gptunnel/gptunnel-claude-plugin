---
name: gptunnel-setup
description: Connect Claude to the user's GPTunneL media library and check that it works — sign-in, which account is connected, what to try first, what this connection cannot do. Use when the user installs the GPTunneL plugin, asks to connect or log in to GPTunneL, when GPTunneL tools are missing or return an authorization error, or when the user asks this connection to make a new image or video. NOT for working with the library itself (use gallery-find-export, gallery-organize or library-review).
---

# Connect GPTunneL

The plugin connects to the GPTunneL MCP server `https://gptunnel.ru/mcp/claude`. Sign-in happens in the browser on gptunnel.ru (OAuth): there is nothing to copy, and the user never types their sign-in details into the chat.

## 1. Check the connection

Call `whoami`.

- **It returns a user id and scopes** — connected. Go to step 3.
- **GPTunneL tools are not available, or the server answers 401 / "needs authentication"** — the user has not signed in. In Claude Code: run `/mcp`, choose `gptunnel`, press Authenticate, sign in on gptunnel.ru and allow access. In Claude apps: Settings → Connectors → GPTunneL → Connect. Then call `whoami` again.
- **403 "MCP access is not enabled for this account"** — the account is signed in, but MCP is not enabled for it yet. Tell the user to write to support@gptunnel.ai; signing in again will not help.
- **Error about a blocked or deleted account** — say so plainly and point to support@gptunnel.ai.

## 2. What the connection allows

This connection works with the user's existing GPTunneL media library: find results, open and download them, sort them into collections. It does not create new media and does not spend the balance; new results are made on gptunnel.ru.

If the user asks for a new image or video: say plainly that this connection cannot make it and nothing was charged, and that it is made on gptunnel.ru. Do not write a ready-to-use description or prompt for it, and do not plan scenes or shots: that is preparing the job, which this plugin does not do. Offer what it can do instead: find similar results already in the library, or, once the new result is made on gptunnel.ru, find it, give the download link and put it into a collection.

## 3. Suggest a first task

Offer three short options in the user's language, for example:

- "Find the video I made last week and give me the download link" (gallery-find-export)
- "Sort my recent results into collections by project" (gallery-organize)
- "Show what is in my library: how many images and videos, what is not sorted" (library-review)

Keep it short: no internals, no tool names in the reply to the user.
