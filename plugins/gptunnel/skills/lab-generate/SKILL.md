---
name: lab-generate
description: Generate images or video with GPTunneL Lab models — pick a model for the task, show the exact price before running, start the generation and return the result. Use when the user asks to create, draw, render, animate or edit an image or video through GPTunneL and no scenario skill fits better. NOT for marketplace cards, product or portrait photoshoots, ad creatives, short videos, logos (use the matching scenario skill), or one-click fixes like background removal (use photo-retouch).
---

# Generate in the GPTunneL Lab

Every generation charges the user's GPTunneL balance. Never start one without showing the price first.

## Steps

1. **Pick the model.** `lab_list_models` (filter `type: image` or `video`, or `search`). Choose by the task: text in the picture, photorealism, editing an input photo, video length. If two models fit, offer the user both with their prices from the list.
2. **Read the model.** `lab_get_model` — params (keys, options, defaults), media inputs and prompt rules. Use only keys and options from here; do not invent params.
3. **Media inputs.** A user file or a link goes through `upload_media` first; pass the returned URL in `inputs` under the input key from `lab_get_model`. Outside URLs are not accepted as inputs.
4. **Quote.** `lab_quote` with the same `model_id`, `prompt`, `params`, `inputs`, `count`. Show `charge_rub` to the user. If `can_run` is false, explain `blocked_reason` (low balance, spend limit of the key) and stop.
5. **Generate.** After the user agrees (or the price is clearly within what they asked for): `lab_generate` with `max_cost_rub` = the quoted `charge_rub` and a fresh `request_id`. On a retry after a network error reuse the same `request_id` — it never charges twice.
6. **Wait for the result.** Poll `lab_get_generation` for each returned id until `done` or `failed`. Video takes minutes: poll every 10–20 seconds, tell the user it is still running.
7. **Return** the result URLs. The generation is also saved in the user's Lab gallery.

## Organization balance

To pay from an organization, call `list_orgs` and pass `org_id` of a row with `personal=false` to `lab_quote` and `lab_generate`. Without `org_id` the personal balance pays.

## Prompt

Write the prompt in the language the model handles best (most models: English), keep the user's intent and every concrete detail they gave. Respect the prompt limit from `lab_get_model`.
