---
name: marketplace-cards
description: Make product cards for Wildberries, Ozon, Yandex Market and other marketplaces from a product photo with GPTunneL — main image, infographic with short selling points, angles and details, product in an interior, a whole product page. Use when the user asks for marketplace cards, listing images, an infographic, "карточки для WB/Ozon", "инфографика", "обложка карточки" or a set of images for a product listing. NOT for brand or lifestyle photos without a listing context (use product-photoshoot), ad banners (use ad-creatives) or video (use short-video).
---

# Marketplace cards

Built on the `lab-generate` steps (model → `lab_get_model` → `lab_quote` → `lab_generate` with `max_cost_rub` → poll). This skill adds what a listing needs.

## 1. Brief — ask only what is missing

Ask at most 3 short questions with options, skip what is already clear:

1. Marketplace: `[Wildberries / Ozon / Yandex Market / several]`
2. What set: `[main image only / main + 4–5 slides / full set with infographics]`
3. Selling points for the infographic: 3–5 short facts (material, size, what is included, key benefit). If the user gave a product description, take them from it and show for confirmation.

A product photo is required: the product must look exactly like the real one. Without a photo, say that a generated product will not match the real item and buyers may complain — proceed only if the user insists.

## 2. Format

- Vertical **3:4** for Wildberries and Ozon slides, at least 900×1200 px. Generate at **2K** resolution when the model offers it: 1K at 3:4 can come out below 900×1200.
- Yandex Market: 3:4 or 1:1, main image on a light clean background.
- Marketplace rules change: if the user mentions a moderation rejection, ask what the marketplace wrote and adjust.

## 3. Pick models

Read `lab_list_models` and `lab_get_model`; choose by these properties, not by name:

- **Keeps the product unchanged from the photo** — the model has an image input (`inputs` of kind `image`) and edits by reference. Nano Banana and Image 2.x (GPT Image) models do this well; Nano Banana 2.1 is the cheapest for a series.
- **Text in the picture** — Image 2.x models usually render text more accurately. Still keep every text block to 2–5 words.
- **A whole product page in one run** — Kling Image 4.0 Product Page builds a long product page from 1–3 photos. It is expensive: quote it and offer as an option, not a default.

## 4. Plan the set

Show a table before any charge: slide, what is on it, ratio, model, price from `lab_quote`. A typical set:

| # | Slide | Content |
|---|---|---|
| 1 | Main | Product large, clean background, 1 short headline at most |
| 2 | Benefits | 3–4 icons or callouts with the selling points |
| 3 | Details | Close-ups of material, texture, fasteners |
| 4 | In use | Product in a fitting interior or in hands |
| 5 | Size / what's included | Dimensions or the box contents |

Show the total and wait for the user's go-ahead.

## 5. Prompt rules

- Pass the product photo in the model's image input; in the prompt say: "keep the product exactly as in the reference photo: shape, colors, logo, label text".
- Write the scene in English for the model; put the on-image text in quotes in the language of the marketplace, e.g. `headline text: "Хлопок 100%"`.
- One text block = 2–5 words. Long sentences come out with typos.
- Name the layout: "vertical 3:4 marketplace product card, product occupies 60% of the frame, headline at the top, three callouts on the right".

## 6. Generate and check

Run slide by slide (`lab_generate`, `max_cost_rub` = that slide's quote, a new `request_id` per slide). Then look at each result:

- Product distorted (wrong logo, extra parts) → regenerate that slide, stronger "keep the product exactly" wording.
- Typos in the Russian text → regenerate with shorter text, or deliver the image without text and offer to add text in an editor.

Never regenerate silently: each retry is charged; tell the user and give the price.

## 7. Deliver

Put all slides into one collection: `gallery_create_collection` named after the product, `gallery_move_generation` for each. Reply with the URLs in slide order and one line per slide.
