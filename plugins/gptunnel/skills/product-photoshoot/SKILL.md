---
name: product-photoshoot
description: Make a product photoshoot from one photo of the product with GPTunneL — studio shots, lifestyle scenes, seasonal and holiday settings, a matching series in one style for a website, catalog or social media. Use when the user asks for product photos, a photoshoot, "предметка", "фотосессия товара", "товар в интерьере", or the same product in several scenes. NOT for marketplace listing slides with text and infographics (use marketplace-cards) or ad banners with an offer (use ad-creatives).
---

# Product photoshoot

Built on the `lab-generate` steps (model → `lab_get_model` → `lab_quote` → `lab_generate` with `max_cost_rub` → poll). This skill adds how to keep the product the same across a series.

## 1. Brief

Ask only what is missing, at most 3 questions with options:

1. Where the photos go: `[website / catalog / social media / everything]` — sets the ratio (website 4:3 or 1:1, catalog 3:4, stories 9:16, feed 4:5 or 1:1).
2. Style: `[clean studio / lifestyle at home / outdoors / seasonal or holiday / premium dark]`. If the user has a brand or reference photos, take the style from them.
3. How many shots.

The product photo is required. A generated product without a reference will not match the real one — say so if there is no photo.

## 2. Pick the model

From `lab_list_models` and `lab_get_model`, pick a model that takes an image input and edits by reference (Nano Banana, Image 2.x). For a series of many shots the cheaper reference model is usually enough; offer a more expensive one only if the first shot loses detail.

## 3. Plan and price

Show a table before charging: shot, scene, ratio, model, price from `lab_quote`, and the total. Wait for the go-ahead.

Scenes that work well:

- Studio: seamless background in a brand color, soft shadow, product at 3/4 angle.
- Lifestyle: product in use, hands in frame, natural window light.
- Context: the room or place where the product belongs (kitchen, bathroom shelf, desk).
- Seasonal: one or two props, not a crowded scene.

## 4. Keep the series consistent

- Pass the same product photo to every shot.
- In every prompt: "keep the product exactly as in the reference: shape, colors, logo, label text, proportions".
- Fix the style in one sentence (light, palette, camera angle) and repeat it word for word in every prompt of the series.
- Generate the first shot, show it, and only then run the rest — the user may want to change the style.

## 5. Check and deliver

Look at each result: wrong logo, changed shape or extra parts → offer a retry with its price, never retry silently. Put the series into a collection (`gallery_create_collection`, `gallery_move_generation`) and reply with the URLs.
