---
name: gallery-organize
description: Sort the user's GPTunneL media library into collections — group results by project, client, type or month, create, rename or recolor collections, move items between them, remove collections. Use when the user asks to tidy up their GPTunneL library, make a collection, group results by project or client, or move items into or out of a collection. NOT for finding a single result or getting download links (use gallery-find-export) or a library overview (use library-review).
---

# Organize the GPTunneL library

Nothing here charges the balance or copies files: moving only changes which collection an item belongs to.

1. **See what exists.** `gallery_list_collections` — names, ids, item counts.
2. **Pick the items.** `gallery_list_generations` with `search`, `type`, `created_after` / `created_before` or `collection_id: ""` (items without a collection). Page with `skip` / `limit` (max 50) until `next_skip` disappears.
3. **Show the plan before changing anything** when more than a few items move: which collection gets which items (count and two or three examples each), which collections will be created. Wait for the go-ahead.
4. **Create or adjust collections.** `gallery_create_collection` (name, optional icon and color); `gallery_update_collection` to rename or change icon and color.
5. **Move.** `gallery_move_generation` with the item id and the collection id; `collection_id: null` takes an item out of its collection.
6. **Remove a collection** with `gallery_delete_collection` only after the user confirms: the collection goes away, its items stay in the library without a collection.
7. **Report:** what moved where, counts per collection.

Good groupings: by project or client (match words in the descriptions), by type (images / video), by month (date filters). Ask which one the user wants if it is not clear.
