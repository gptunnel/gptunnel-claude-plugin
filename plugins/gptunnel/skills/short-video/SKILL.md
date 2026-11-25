---
name: short-video
description: Make a short vertical video with GPTunneL — Reels, Shorts, TikTok, stories, a product video for a marketplace card — from a photo or a text idea, optionally with sound effects. Use when the user asks to animate a photo, make a short video, a reel, a clip for stories, "оживи фото", "видео для карточки", "сделай рилс". NOT for long edited videos or several scenes cut together with music (use workflow-templates), or still images (use lab-generate).
---

# Short video

Built on the `lab-generate` steps (model → `lab_get_model` → `lab_quote` → `lab_generate` with `max_cost_rub` → poll). Video is more expensive than images and takes minutes — plan carefully before charging.

## 1. Brief

Ask only what is missing:

1. Where it goes: `[Reels / Shorts / TikTok / stories / marketplace card / other]` — almost always vertical **9:16**; a marketplace video may be 3:4 or 1:1, ask.
2. Start from: `[a photo / only a text idea]`. A photo gives control over how the product or person looks — recommend it.
3. Length: most models do 4–15 seconds per clip. Ask how long, and say that longer means more expensive.

## 2. Pick the model

`lab_list_models` with `type: video`, then `lab_get_model` for the candidates. Choose by:

- **Image to video** — the model has a first-frame input (often `first_frame`); some also take a last frame or reference images.
- **Duration and resolution** offered by the model, and whether the price grows with them (check with `lab_quote`).
- **Sound** — some models generate audio themselves; check params.

Quote two models at the same settings — a fast cheap one and a high-quality one — and let the user choose.

## 3. Prompt

Describe motion, not the picture: the photo already sets how it looks. One main action and one camera move: "the camera slowly orbits the bottle, light glints on the glass, steam rises from the cup". Avoid many events in 5 seconds.

## 4. Quote, generate, wait

`lab_quote` → show the price → `lab_generate` with `max_cost_rub`. Video takes several minutes: poll `lab_get_generation` every 15–20 seconds and tell the user it is still running.

## 5. Sound

If the model made no sound and the user wants it, the @SoundEffect app makes a sound effect from a text description (`app_run` with `app_code` `@SoundEffect`, `prompt` describing the sound, `params.duration_seconds` equal to the clip length, `max_cost_rub` = price per second from `apps_list` × duration; poll `app_get_task`). Joining sound and video is done in the user's editor, or with a workflow (see workflow-templates).

## 6. Deliver

Return the video URL and say what to change if the result is not right (motion, camera, length). A retry is charged again — show the price.
