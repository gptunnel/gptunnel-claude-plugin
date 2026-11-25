---
name: workflow-templates
description: Find a ready GPTunneL workflow template for the user's task, copy it to their account and fill in their inputs, so it is ready to run in the GPTunneL editor — marketplace covers, cartoon from a photo, music video, fashion lookbook, 3D object, camera fly-around, photo enhancement, background or watermark removal. Use when the user asks for a template, "шаблон", a ready pipeline, or a task that ready templates cover. NOT for designing a new workflow from scratch (use workflow-build).
---

# Workflow templates

A template is a ready workflow published by GPTunneL or the community. Copying it is free and does not spend the balance.

## 1. Find

`list_templates` returns published templates by popularity (`limit` up to 100, `offset` for the next page). Match the user's task against each template's title and description (they are often in Russian: "обложка", "мультфильм", "клип", "3D"). Show 2–4 matches: name, what it makes, the preview (`thumbnail`). If nothing fits, offer to build one (workflow-build).

## 2. Copy

`fork_template` with the template id → a new workflow in the user's account (pass `org_id` to copy into an organization).

## 3. Fill in the inputs

`get_workflow` → find the input nodes (photo, text, prompt). Ask the user only for those. Files go through `upload_media` with the `workflow_id` of the copy. Write the values with `update_workflow`: it replaces the whole graph, so send the graph from `get_workflow` with only the input values changed.

## 4. Hand over

Tell the user the workflow is in their account, ready to run in the GPTunneL editor on gptunnel.ru, and which inputs you filled. Next time they only change the inputs.
