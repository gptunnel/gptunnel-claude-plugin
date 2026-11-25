---
name: ad-creatives
description: Make ad creatives with GPTunneL — banners for Yandex Direct, VK Ads, Telegram Ads and social media in several sizes at once, with A/B variants of the visual and the headline. Use when the user asks for an ad banner, creatives, "креативы для таргета", "баннер для Директа", ad images in several formats, or variants for an A/B test. NOT for marketplace listing slides (use marketplace-cards), a plain product photoshoot (use product-photoshoot) or video ads (use short-video).
---

# Ad creatives

Built on the `lab-generate` steps (model → `lab_get_model` → `lab_quote` → `lab_generate` with `max_cost_rub` → poll).

## 1. Brief

Ask only what is missing, at most 3 questions:

1. Where the ad runs: `[Yandex Direct / VK Ads / Telegram Ads / social feed and stories]`.
2. What is advertised and the one main message: product, offer, discount, deadline.
3. How many variants for the test: `[2 / 3 / 4]`.

If the user has a product photo, a logo or brand colors — ask for them, use them as references.

## 2. Formats

Make one master design, then adapt it, rather than generating each size from scratch:

| Placement | Ratios |
|---|---|
| Yandex Direct (images) | 1:1, 16:9, 4:3 (vertical 3:4 or 9:16 if the user needs it) |
| VK Ads | 1:1, 16:9, 9:16 |
| Telegram Ads | ask the user: rules and formats change |
| Feed / stories | 1:1 or 4:5 / 9:16 |

Use only ratios that the chosen model offers in `lab_get_model`; if a ratio is missing, say so and propose the closest one. Ad platforms change requirements — if the user has an up-to-date spec, follow it.

## 3. Variants for A/B

Change one thing per variant, so the test shows what worked: either the visual (scene, angle, color) with the same headline, or the headline with the same visual. Show the plan as a table: variant, what differs, ratios, model, price from `lab_quote`, total. Wait for the go-ahead.

## 4. Text on the banner

- Headline 2–5 words, in quotes in the prompt, in the language of the ad. Longer text comes out with typos.
- Leave room for the text: "empty space on the left third for the headline".
- Many ad platforms limit how much of the image text may cover; offer a variant without text that the user overlays in the ad editor.
- Do not put prices, discounts or legal claims into the image unless the user gave the exact wording.

## 5. Check and deliver

Check each banner: typos, distorted product or logo, text cut off at the edge. Offer retries with their price. Put all variants into one collection named after the campaign and reply with a table: variant → ratio → URL.
