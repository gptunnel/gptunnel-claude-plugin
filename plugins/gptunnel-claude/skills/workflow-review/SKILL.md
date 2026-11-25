---
name: workflow-review
description: Explain what an existing GPTunneL workflow does and check it for mistakes — unconnected inputs, empty required parameters, incompatible ports, unused nodes, steps that can be simplified. Use when the user asks "what does this workflow do", "why does my workflow fail", to review, document or clean up a workflow, or to compare two workflows. NOT for building a new workflow (use workflow-build) or finding a template (use workflow-templates).
---

# Review a GPTunneL workflow

Reading changes nothing. Edit only after the user agrees to the fixes.

## 1. Find the workflow

`list_workflows` (with `org_id` for an organization). If the user gave a link or a name, match it; otherwise show recent workflows and ask which one.

## 2. Read and explain

`get_workflow` → nodes and edges. For node types you do not know, `get_node_type`. Explain in the user's language, in the order data flows: what goes in, what each step does, what comes out. Keep it to one line per node; skip technical ids.

## 3. Check

Go through the graph and list findings, most important first:

- An input port of a working node has no edge and no value in `data`.
- A required parameter from `get_node_type` is empty, or a value is not among its allowed options.
- An edge connects ports of different types.
- Nodes that lead nowhere (no path to an output) — they spend time and may spend money when the workflow runs.
- Repeated identical steps that could be one node with several outputs.

For each finding: where (node name), what is wrong, the proposed fix.

## 4. Fix

If the user agrees, apply the fixes with `update_workflow` — it replaces the whole graph, so send every node and edge from `get_workflow` with only the fixes changed. Then call `get_workflow` again and confirm what changed.
