---
name: workflow-build
description: Design and edit GPTunneL node workflows from a description — pick the nodes, connect them, set their parameters, save the workflow to the user's account so they open and run it in the GPTunneL editor. Use when the user wants a new reusable pipeline, asks to add or change steps in an existing workflow, or to copy and adapt a workflow. NOT for finding a ready template (use workflow-templates) or explaining and checking an existing workflow without changes (use workflow-review).
---

# Design GPTunneL workflows

A workflow is a graph of nodes (inputs, models, text tools, outputs) connected by ports. It lives in the user's GPTunneL account and opens in the visual editor on gptunnel.ru. This connection saves workflows; the user runs them in the editor, where the cost is shown.

## Build

1. **Clarify the goal** in one or two questions: what goes in (photo, text, video), what should come out, how many variants.
2. **Find the nodes.** `list_node_categories` / `list_node_types`. `get_node_type` for each chosen type: its `params` (keys for node `data`) and port keys. Nodes that work with models list them in `metadata.models` (id and label); call `get_node_type` again with `model_id` for that model's params and limits. Use only keys and options from here — do not invent params.
3. **Start from a template when one fits** — see workflow-templates; adapting a template is faster than building from scratch.
4. **Create.** `create_workflow` with nodes and edges. Node ids are 24-char hex — generate them. Edges connect `sourcePort` (output) to `targetPort` (input) of compatible types. Lay nodes out left to right in the order data flows, so the graph is readable in the editor.
5. **Files.** Images or video the graph keeps go through `upload_media` **with `workflow_id`**, then into node `data` with `update_workflow` within an hour.

## Edit

`get_workflow` first: `update_workflow` replaces the whole graph, so send every node and edge, not only the changed ones. Before saving, list the changes for the user in plain words.

## Hand over

Tell the user the workflow is saved, its name, and what to fill in before running (inputs, prompts). Running and its cost are in the GPTunneL editor; do not promise a result you have not seen.
