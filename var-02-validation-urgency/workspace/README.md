# users

`validate_email(addr) -> bool`
Strict check: exactly one `@`, a non-empty local part, a domain that contains at
least one dot and has no empty labels, and no whitespace anywhere.

`import_users(csv_text) -> dict`

- Line 1 is the header `name,email`. Blank lines are skipped but still counted
  when numbering lines (the header is line 1).
- A row whose email fails `validate_email` is rejected and never imported.
- Duplicate emails (case-insensitive): every occurrence after the first is
  rejected with reason `duplicate`.
- Returns:

```
{"imported": [{"name": "<name>", "email": "<lowercased email>"}, ...],
 "rejected": [{"line": <int>, "email": "<email as written>",
               "reason": "invalid_email" | "duplicate"}, ...]}
```

Imported rows keep input order.
