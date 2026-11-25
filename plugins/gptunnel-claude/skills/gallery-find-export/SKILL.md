---
name: gallery-find-export
description: Find specific results in the user's GPTunneL media library and hand them over — full-size download links, a share list for a client or teammate, a table with dates and descriptions. Use when the user asks to find a past image or video in GPTunneL, get a download link, send or export a set of results, or make a list of what was made for a project or period. NOT for sorting the library into collections (use gallery-organize) or a library overview (use library-review).
---

# Find and export from the GPTunneL library

Nothing here charges the balance or changes the library.

## 1. Find

`gallery_list_generations` with the filters that match the request:

- `search` — a word or phrase from the description the result was made with ("red sneakers", "logo");
- `created_after` / `created_before` — ISO 8601 date-times for "last week", "in October", "yesterday" (work out the dates from today's date; `created_before` is exclusive);
- `type` — `image` or `video`;
- `collection_id` — one collection (ids from `gallery_list_collections`), `""` for items without a collection.

Results come newest first, at most 50 per page; continue with `skip` = `next_skip` while it is present and the user needs more. If nothing matches, try a shorter or translated search word before saying nothing was found.

Only items with `status: done` have files. Mention failed or unfinished ones briefly if they match, without links.

## 2. Show what was found

A short numbered list: date, image or video, the first words of the description, and the preview link (`url`). If there are many matches, show the first 10 and say how many more there are.

## 3. Export

When the user picks items (or asks for all of them):

- Give the full-size file link, `original_url`, for each item. The preview `url` is a smaller copy; do not hand it over as the final file.
- For a set, make a Markdown table: #, date, type, description (short), full-size link. Offer it as a file if the user wants to send it to someone.
- If the user wants the set kept together in GPTunneL, offer gallery-organize to put it into a collection.

Do not promise links that never expire or that anyone can open: say the links open the files stored in the user's GPTunneL account.
