---
name: gallery-organize
description: Find and organize generations in the GPTunneL Lab gallery — search by prompt, sort into collections, rename or remove collections. Use when the user asks to find a past image or video, or to tidy up their GPTunneL gallery. NOT for generating new images (use lab-generate).
---

# GPTunneL gallery

Nothing here charges the balance or copies files.

1. **Find.** `gallery_list_generations` — filter by `search` (substring of the prompt), `type`, `collection_id` (`""` = without a collection). Page with `skip` / `limit` (max 50).
2. **Collections.** `gallery_list_collections` for existing ones; `gallery_create_collection` for a new one; `gallery_update_collection` to rename or change icon and color.
3. **Sort.** `gallery_move_generation` puts a generation into a collection, `collection_id: null` takes it out.
4. **Delete a collection.** `gallery_delete_collection` removes only the collection — confirm with the user first; generations stay in the gallery.

When sorting many generations, show the plan (which ids go where) before moving.
