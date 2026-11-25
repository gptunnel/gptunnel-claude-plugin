# Evals

Behavior checks with `claude plugin eval`. The GPTunneL MCP server is mocked: `mocks/gptunnel/<tool>.md` is the canned answer for that tool; a case can override it in `<case>/mocks/gptunnel/`. Nothing reaches gptunnel.ru and nothing is charged.

Evals live outside the plugin folders (the Anthropic directory rejects eval files inside a submitted plugin). `scripts/eval.sh` copies the plugin and its evals into a temp folder and runs there; each run is a Claude session on your credential:

```bash
scripts/eval.sh gptunnel --runs 1
```

Plugin MCP tools are named `mcp__plugin_gptunnel_gptunnel__<tool>`. For "the tool must not be called" use `tool_used` with both `min: 0` and `max: 0` (`min` defaults to 1).

| Case | Checks |
|---|---|
| `lab-quote-before-generate` | `lab_get_model` and `lab_quote` before `lab_generate`; `max_cost_rub` equals the quote |
| `lab-blocked-stops` | quote says `can_run: false` → no generation, the user hears why |
| `retouch-bg-remove` | file uploaded first, then `@BGRemover` with `max_cost_rub`, no Lab generation |
| `marketplace-plan-before-charge` | `marketplace-cards` skill fires; plan with prices and total, nothing charged without confirmation |
