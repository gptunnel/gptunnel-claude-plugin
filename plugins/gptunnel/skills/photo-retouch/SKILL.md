---
name: photo-retouch
description: Fix and clean up photos with GPTunneL one-click apps — remove the background, improve quality and upscale, restore an old photo, colorize a black-and-white photo. Use when the user asks to remove a background, "убери фон", improve, sharpen or enlarge a photo, restore or colorize an old photo, "раскрась ч/б фото". NOT for changing what is in the photo — new scene, new clothes, adding objects (use lab-generate or product-photoshoot).
---

# Photo retouch with apps

GPTunneL apps are one-click tools with a fixed task and price: no model to choose, no prompt to write. Run with `app_run`, wait with `app_get_task`.

## 1. Pick the app

Call `apps_list` to get current apps, prices and params. Typical ones:

| Task | App |
|---|---|
| Remove the background | @BGRemover |
| Improve quality, upscale, restore an old photo | @PhotoBooster (`mode`: quality / restore / colorize; `upscale_factor` for quality) |
| Colorize a black-and-white photo | @TrueColor (fixed price) or @PhotoBooster `mode: colorize` |

If no app fits (the user wants to change the content of the photo, fix white balance, retouch skin), switch to lab-generate with a reference-editing model.

## 2. Input

The photo goes through `upload_media` first; pass the returned URL as `image`. Outside links are not accepted.

## 3. Price and run

- Fixed price apps: tell the user the price from `apps_list`.
- Variable price (@PhotoBooster depends on the mode and photo size): agree an upper bound with the user and pass it as `max_cost_rub` — the run never charges more. If the price is higher, the refusal names the exact price: show it and ask before running again.

`app_run` with `app_code`, `image`, `params` only from `apps_list`, `max_cost_rub`, a new `request_id` (reuse it only to retry after a network error), and `org_id` if an organization pays. If the answer says the balance is too low or the limit is reached, tell the user and stop.

## 4. Wait and deliver

Poll `app_get_task` until it is done or failed (usually seconds). Return the result URL.

For several photos: show the count × price as a total first, then run them one by one.

Chains work well: background removal → product-photoshoot to put the product into a new scene; @PhotoBooster restore → colorize for an old family photo.
