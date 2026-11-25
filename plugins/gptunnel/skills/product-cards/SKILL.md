---
name: product-cards
description: Make a set of marketplace product images or ad creatives from one product photo with GPTunneL — clean background shots, lifestyle scenes, banners in several aspect ratios. Use when the user has a product photo and needs listing images or a creative series.
---

# Product cards and creative series

Built on the `lab-generate` steps; this skill adds the plan for a series.

1. **Brief.** Ask only what is missing: the marketplace or channel (it decides aspect ratios — e.g. 3:4 for listings, 1:1 and 9:16 for ads), how many images, the style.
2. **Upload** the product photo with `upload_media` (temporary file is fine for Lab inputs).
3. **Model.** In `lab_list_models` / `lab_get_model` pick a model that accepts an input image and keeps the product unchanged (image editing / reference input). Check the aspect ratio options.
4. **Plan the series** as a table: scene, aspect ratio, prompt. Quote every row with `lab_quote` and show the total before running.
5. **Generate** row by row with `lab_generate` (`max_cost_rub` from the row's quote), poll `lab_get_generation`.
6. **Collect** the results into one collection: `gallery_create_collection` named after the product, then `gallery_move_generation` for each result.
7. Return the URLs grouped by aspect ratio.

The product itself (shape, logo, label text) must stay as on the photo: say so in every prompt.
