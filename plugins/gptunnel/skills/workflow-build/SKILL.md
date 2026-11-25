---
name: workflow-build
description: Build, edit and run GPTunneL node workflows — pipelines that chain models (prompt → image → upscale → video). Use when the user wants a reusable pipeline, a batch of similar results, or to change or run an existing GPTunneL workflow. NOT for a single image or video (use lab-generate) or when a ready template fits (use workflow-templates).
---

# GPTunneL workflows

A workflow is a graph of nodes (models, inputs, text tools) connected by ports. It lives in the user's GPTunneL account and opens in the visual editor.

## Build

1. `list_node_categories` / `list_node_types` — find the nodes for the task. `get_node_type` for each chosen type: its `params` (keys for node `data`) and port keys. Generation nodes list their models in `metadata.models` (id and label only); call `get_node_type` again with `model_id` to get that model's params and constraints.
2. Start from a template when one fits: `list_templates` → `fork_template`.
3. Otherwise `create_workflow` with nodes and edges. Node ids are 24-char hex — generate them. Edges connect `sourcePort` (output) to `targetPort` (input) of compatible types.
4. Files the graph keeps (input images, video) go through `upload_media` **with `workflow_id`**, then into node `data` with `update_workflow` within an hour.

## Edit

`get_workflow` first: `update_workflow` replaces the whole graph, so send every node and edge, not only the changed ones.

## Run

Running charges the balance for every paid node.

1. Tell the user which paid nodes will run.
2. `run_workflow` → `executionId`.
3. Poll `get_execution` until `completed`, `failed` or `cancelled`; report per-node errors and cost.
4. A failed node: fix the graph and `run_workflow` with `from_node_id` — upstream results are reused, not paid again.
