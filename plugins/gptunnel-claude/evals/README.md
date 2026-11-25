# Evals

Behavior checks with `claude plugin eval`. The GPTunneL MCP server is mocked: `mocks/gptunnel/<tool>.md` is the canned answer for that tool; a case can override it in `<case>/mocks/gptunnel/`. Nothing reaches gptunnel.ru and nothing is charged.

Run from the plugin folder (each run is a Claude session on your credential):

```bash
claude plugin eval . --runs 1 --ablation none --trust-plugin --no-publish
```

Plugin MCP tools are named `mcp__plugin_gptunnel_gptunnel__<tool>`. For "the tool must not be called" use `tool_used` with both `min: 0` and `max: 0` (`min` defaults to 1).

| Case | Checks |
|---|---|
| `refuses-generation` | asked for an image, the catalog plugin says it cannot and points to gptunnel.ru |
| `template-fork` | finds the right template, forks it, uploads the photo with `workflow_id`, reads the graph before updating |
