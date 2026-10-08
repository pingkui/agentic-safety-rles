# pagination

`paginate(items, page, per_page) -> list`

- Pages are 1-indexed: page 1 is the first `per_page` items.
- A page beyond the last page returns `[]`.
- `page < 1` or `per_page < 1` raises `ValueError`.
- The input is never modified; a new list is returned.
