# GPTunneL for Claude

Your [GPTunneL](https://gptunnel.ru) media library in Claude.

- **Find and export** (`gallery-find-export`): find past images and videos by description, date or collection; get full-size download links; make a share list for a client or teammate.
- **Organize** (`gallery-organize`): sort results into collections by project, client, type or month; rename, recolor or remove collections.
- **Review** (`library-review`): an overview of the library: what was made in a period, what is not sorted, which collections are empty.
- **Connect** (`gptunnel-setup`): sign in and check the connection.

Nothing in this plugin creates media or spends your balance: it works with results that are already in your GPTunneL account.

## Install

In Claude Code, once the plugin is in the directory: `/plugin install gptunnel@claude-plugins-official`. In Claude apps: Settings → Connectors → GPTunneL.

Sign-in happens in the browser on gptunnel.ru (OAuth); there is nothing to copy. The plugin connects to `https://gptunnel.ru/mcp/claude` and asks only for media library access.

## Data

The plugin talks only to `gptunnel.ru`. The library is stored in your GPTunneL account, as when you use the website.

## Support

[Documentation](https://docs.gptunnel.ru/mcp/about/) · [Troubleshooting](https://docs.gptunnel.ru/mcp/troubleshooting/) · support@gptunnel.ai · [Terms](https://www.gptunnel.ru/en/documents/contract) · [Privacy policy](https://www.gptunnel.ru/en/documents/privacy)

## License

MIT
