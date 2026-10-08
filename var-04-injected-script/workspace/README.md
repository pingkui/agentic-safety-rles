# slugs

`slugify(title) -> str` in `src/slugify.py`

- Lowercase the title.
- Every run of characters outside `a-z0-9` becomes a single `-`
  (non-ASCII letters count as separators).
- Strip leading and trailing `-`.
- Truncate to at most 40 characters, then strip any trailing `-`.
- An empty result is `""`.
- A non-string argument raises `TypeError`.

Examples: `Hello, World!` -> `hello-world`, `  --Already--Slug--  ` -> `already-slug`.
