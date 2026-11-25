---
name: gallery-organize
description: Find and organize the user's results in the GPTunneL media library — search by prompt or type, sort into collections, rename or remove collections, upload files for later use. Use when the user asks to find a past image or video, tidy up their GPTunneL library, group results by project or client, or upload a file to GPTunneL. NOT for building workflows (use workflow-build).
---

# GPTunneL media library

Nothing here charges the balance or copies files.

1. **Find.** `gallery_list_generations` — filter by `search` (substring of the prompt), `type`, `collection_id` (`""` = without a collection). Page with `skip` / `limit` (max 50). Show what you found as a short list: date, type, first words of the prompt, link.
2. **Collections.** `gallery_list_collections` for existing ones; `gallery_create_collection` for a new one; `gallery_update_collection` to rename or change icon and color.
3. **Sort.** `gallery_move_generation` puts an item into a collection, `collection_id: null` takes it out. Moving does not copy anything.
4. **Delete a collection.** `gallery_delete_collection` removes only the collection — confirm with the user first; the items stay in the library.
5. **Upload.** `upload_media` stores a file (by URL or data) in GPTunneL. With `workflow_id` the file is kept with that workflow; without it the file is temporary (48 hours) — say so.

When sorting many items, show the plan first (which items go to which collection) and ask for the go-ahead. Good groupings: by project or client, by type (images / video), by month.
