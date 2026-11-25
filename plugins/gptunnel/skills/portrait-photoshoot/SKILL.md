---
name: portrait-photoshoot
description: Make a portrait photoshoot from the user's own photos with GPTunneL — business portrait, avatar, profile photo, styled or themed shoot, new outfit or background — keeping the face recognizable. Use when the user asks for an avatar, a business photo for a CV or LinkedIn, "фото на аватарку", "нейрофотосессия", "сделай меня в образе…". NOT for photos of other real people without their consent, product photos (use product-photoshoot) or simple fixes of an existing photo (use photo-retouch).
---

# Portrait photoshoot

Built on the `lab-generate` steps (model → `lab_get_model` → `lab_quote` → `lab_generate` with `max_cost_rub` → poll).

## 1. Photos and consent

- Ask for 1–3 clear photos of the face: good light, front or 3/4, no sunglasses, no heavy filters. More good references → closer likeness, if the model accepts several.
- Work only with the user's own photos or photos of people who agreed. If the photo is of a public person or someone else without consent, decline politely.
- Children's photos: only at the parent's request, no adult or provocative styles.

## 2. Brief

Ask only what is missing:

1. Purpose: `[business portrait / avatar / social media / themed shoot]`.
2. Style or image: clothes, background, mood. Offer 3 ready ideas if the user does not know.
3. Ratio: avatar 1:1, CV 3:4, stories 9:16.

## 3. Model and likeness

Pick a model with image input that edits by reference (`lab_get_model` shows how many reference images it accepts). In the prompt: "keep the person's face exactly as in the reference photos: facial features, face shape, eye color, skin tone, hairline". Change only what the user asked: clothes, background, light.

## 4. Plan, test, series

Show the plan with prices and total. Generate one image first and ask whether the likeness is good. Only then run the rest of the series. If the likeness is weak, suggest better reference photos before spending more.

## 5. Deliver

Put the shoot into a collection and return the URLs. Do not describe the person's appearance in the reply beyond what is needed.
