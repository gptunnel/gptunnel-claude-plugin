---
name: workflow-templates
description: Find a ready GPTunneL workflow template for a multi-step task, copy it to the user's account, fill in their inputs and run it — marketplace covers, cartoon from a photo, music video, fashion lookbook, 3D object, camera fly-around video, photo enhancement, background or watermark removal. Use when the task needs several steps chained together, the user mentions a template or "шаблон", or a result needs several models one after another. NOT for one image or one video (use lab-generate or a scenario skill) or building a new workflow from scratch (use workflow-build).
---

# Workflow templates

A template is a ready workflow made by GPTunneL or the community. Copying it is free; running it charges the balance for every generation node inside.

## 1. Find a template

`list_templates` returns published templates by popularity (page with `limit` up to 100 and `offset`). Match the user's task against each template's title and description (they are often in Russian: "обложка", "мультфильм", "клип", "3D"). Show 2–4 matching templates: name, what it makes, the preview (`thumbnail`). Let the user choose. If nothing fits, offer workflow-build.

## 2. Copy

`fork_template` with the template id → a new workflow in the user's account. Tell the user it is saved and they can open it on gptunnel.ru.

## 3. Fill in the inputs

`get_workflow` → find the input nodes (photo, text, prompt). Ask the user only for those. Files go through `upload_media` with the `workflow_id` of the copy (then they are stored with the workflow). Write the values with `update_workflow`: it replaces the whole graph, so send the graph from `get_workflow` with only the input values changed.

## 4. Price before running

A workflow runs several paid generations. Before `run_workflow`, tell the user which generation nodes will run and that each is charged. If the template description or the nodes show models, quote them with `lab_quote` and give an approximate total. Ask for the go-ahead.

## 5. Run and wait

`run_workflow` → poll `get_execution` every 10–20 seconds; video and music steps take minutes. Report progress by node. If a node fails, show the error; `retry_node` reruns only that node, nodes after it are not restarted (it is charged again — say so).

## 6. Deliver

Return the outputs of the final nodes. The workflow stays in the user's account: next time they only change the inputs and run it again.
