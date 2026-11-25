# GPTunneL plugin for Claude Code, Codex and Cursor

Marketplace cards, product and portrait photoshoots, ad creatives, short videos, logos and photo retouch with [GPTunneL](https://gptunnel.ru) models — right from your coding agent. The agent shows the price before every generation and pays from your GPTunneL balance.

## Install

**Claude Code**

```
/plugin marketplace add gptunnel/gptunnel-claude-plugin
/plugin install gptunnel@gptunnel
```

**Codex**

```
codex plugin marketplace add gptunnel/gptunnel-claude-plugin
codex plugin add gptunnel@gptunnel
```

**Cursor** — add `https://github.com/gptunnel/gptunnel-claude-plugin` in Settings → Plugins, or with the CLI: `agent plugin marketplace add https://github.com/gptunnel/gptunnel-claude-plugin`.

**Any other MCP client** — add an HTTP (streamable) MCP server `https://gptunnel.ru/mcp`.

Agents can install it themselves: point yours at [INSTALL_FOR_AGENTS.md](https://github.com/gptunnel/gptunnel-claude-plugin/blob/main/INSTALL_FOR_AGENTS.md).

Sign-in is OAuth in the browser — no API key to copy. Claude Code: `/mcp` → `gptunnel` → Authenticate. Codex: `codex mcp login gptunnel`. Cursor: Settings → MCP → Connect.

## What you can ask

| Skill | Example request |
|---|---|
| `marketplace-cards` | "Make 5 Wildberries cards from this product photo" |
| `product-photoshoot` | "Put my candle in a cozy winter interior, 4 shots for the website" |
| `ad-creatives` | "Banners for VK Ads in 1:1, 16:9 and 9:16, two variants for an A/B test" |
| `short-video` | "Animate this photo into a 5-second vertical reel" |
| `photo-retouch` | "Remove the background", "Restore and colorize this old photo" |
| `portrait-photoshoot` | "A business portrait for my CV from these selfies" |
| `logo-and-stickers` | "Three vector logo concepts for a coffee shop" |
| `workflow-templates` | "Make a cartoon from my photo with a ready template" |
| `lab-generate` | Any image or video with a model of your choice |
| `workflow-build` | Build a reusable multi-step pipeline |
| `gallery-organize` | "Find last week's banners and put them into a collection" |
| `gptunnel-setup` | Connect and check the account |

## Data and payments

The plugin talks only to `gptunnel.ru`. Prompts, uploaded files and results are stored in your GPTunneL account, as when you use the website. Generations, apps and workflow runs are paid from your GPTunneL balance (or an organization balance you choose). The agent shows the price before charging, and every paid call carries a price cap, so it never charges more than shown. Limits and spending caps are set on the MCP page of your account.

## Support

[Documentation](https://docs.gptunnel.ru/mcp/about/) · [Troubleshooting](https://docs.gptunnel.ru/mcp/troubleshooting/) · support@gptunnel.ai · [Terms](https://www.gptunnel.ru/en/documents/contract) · [Privacy policy](https://www.gptunnel.ru/en/documents/privacy)

## License

MIT
