# GPTunneL plugin for Claude Code

Generate images and video in the [GPTunneL](https://gptunnel.ru) Lab, build and run node workflows, and organize your gallery without leaving Claude Code.

## Install

```
/plugin marketplace add gptunnel/gptunnel-claude-plugin
/plugin install gptunnel@gptunnel
```

On first use Claude Code opens the browser to sign in to GPTunneL (OAuth). No API key to copy.

## What is inside

- **MCP server** `https://gptunnel.ru/mcp` — Lab generation, workflows, gallery, file upload.
- **Skills:**
  - `lab-generate` — pick a model, show the exact price, generate, return the result;
  - `workflow-build` — build, edit and run workflows;
  - `gallery-organize` — find generations and sort them into collections;
  - `product-cards` — a series of marketplace images or ad creatives from one product photo.

## Data and payments

The plugin talks only to `gptunnel.ru`. Prompts, uploaded files and results are stored in your GPTunneL account, as when you use the website. Generations and workflow runs are paid from your GPTunneL balance (or an organization balance you choose). Claude shows the price before every generation. Limits and spending caps are set on the MCP page of your account.

## Support

[Documentation](https://docs.gptunnel.ru/mcp/about/) · support@gptunnel.ai · [Terms](https://www.gptunnel.ru/en/documents/contract) · [Privacy policy](https://www.gptunnel.ru/en/documents/privacy)

## License

MIT
