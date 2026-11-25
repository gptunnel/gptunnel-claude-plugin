---
name: logo-and-stickers
description: Make a logo, icon, vector illustration or a sticker pack with GPTunneL — several logo concepts in vector, icons in one style, stickers with one character. Use when the user asks for a logo, an icon set, a vector illustration, SVG, "логотип", "стикеры для Telegram", "стикерпак". NOT for full brand books, photo-like images (use lab-generate) or marketplace cards (use marketplace-cards).
---

# Logo and stickers

## Logo and icons

Built on the `lab-generate` steps (model → `lab_get_model` → `lab_quote` → `lab_generate` with `max_cost_rub` → poll).

1. **Brief**: name (exact spelling), what the company does, 2–3 words about character (strict, playful, premium), colors if any, where it will be used (site, app icon, sign).
2. **Model**: for logos and icons prefer a model that outputs vector — in `lab_get_model` look for a vector type or style option (Recraft has `type: vector`). Vector scales without loss and can be edited.
3. **Concepts**: offer 3–4 different directions (lettering only, symbol + text, monogram, mascot). Show the plan with prices and the total, then generate.
4. **Prompt**: "flat vector logo, simple shapes, 2 colors, white background, no gradients, no mockup"; the name in quotes. Short names render most reliably; check the spelling of every letter in the result.
5. **Iterate** on the chosen concept only: color, thickness, simplification. Each retry is charged — show the price.

Say honestly: a generated logo is a starting point; for trademark registration the user should check it is not similar to existing marks.

## Sticker pack

1. **Character**: a mascot, a description, or the user's own photo. For a pack, the character must look the same in every sticker.
2. **One quick sticker from a text** — the @Stiker app: price from `apps_list`, `app_run` with `app_code` `@Stiker`, a `prompt` describing the sticker, `max_cost_rub`; poll `app_get_task`. It draws from text only, so the same character is not guaranteed across stickers.
3. **A pack with one character** (or from a photo): generate a base image of the character in the Lab first (a model with image input if there is a photo), get the user's approval, then make each emotion with the base image as a reference: "same character, same style, same colors, emotion: laughing". White background, thick outline; @BGRemover makes the background transparent.
4. **Plan**: list of emotions (8–12 for a starter pack), price each and the total before running.

Deliver as a collection; tell the user that Telegram stickers are uploaded via @Stickers bot as 512×512 PNG/WebP — they may need resizing.
