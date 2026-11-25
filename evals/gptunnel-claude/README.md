# Evals

Behavior checks with `claude plugin eval`. The GPTunneL MCP server is mocked: `mocks/gptunnel/<tool>.md` is the canned answer for that tool; a case can override it in `<case>/mocks/gptunnel/`. Nothing reaches gptunnel.ru and nothing is charged.

Evals live outside the plugin folders (the Anthropic directory rejects eval files inside a submitted plugin). `scripts/eval.sh` copies the plugin and its evals into a temp folder and runs there; each run is a Claude session on your credential:

```bash
scripts/eval.sh gptunnel-claude --runs 1
```

Plugin MCP tools are named `mcp__plugin_gptunnel_gptunnel__<tool>`. For "the tool must not be called" use `tool_used` with both `min: 0` and `max: 0` (`min` defaults to 1).

| Case | Checks |
|---|---|
| `refuses-generation` | asked for an image, the catalog plugin says it cannot and points to gptunnel.ru |
| `find-export` | finds the video by description and period, hands over the full-size `original_url`, changes nothing |
| `organize-plan-first` | lists items before moving, moves only matching finished results (or asks first), leaves the rest alone |
