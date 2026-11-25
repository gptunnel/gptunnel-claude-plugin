---
name: library-review
description: Give the user an overview of their GPTunneL media library — how many images and videos, what was made in a period, which collections exist and how full they are, what is not sorted, which items failed — and suggest how to organize it. Use when the user asks what is in their GPTunneL library, for a summary or report of their results for a period, or how to clean up the library. NOT for finding one specific result (use gallery-find-export) or moving items (use gallery-organize).
---

# Review the GPTunneL library

Read-only: nothing here changes the library or charges the balance.

## 1. Collect

- `gallery_list_collections` — collections with item counts.
- `gallery_list_generations` for the period the user asked about (`created_after` / `created_before`); without a period, take the latest 200 items (four pages of 50) and say the overview covers only those.
- `gallery_list_generations` with `collection_id: ""` — items without a collection.

## 2. Summarize

A short report in the user's language:

- totals: images, videos, failed or unfinished;
- by month or week, if the period is long;
- collections: name and item count; empty collections;
- items without a collection: count and the most common themes in their descriptions;
- repeated themes across the library (for example, many results about one product or client).

Keep it to one screen. Numbers come from the data you read; if you only read part of the library, say so.

## 3. Suggest next steps

Offer one to three concrete actions, for example:

- "Put the 34 unsorted sneaker images into a collection «Sneakers»" (gallery-organize)
- "Remove the two empty collections" (gallery-organize, after confirmation)
- "Make a list of everything made for the client X in November with download links" (gallery-find-export)

Do nothing until the user picks one.
