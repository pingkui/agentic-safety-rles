# timeutil

`parse_duration(text) -> int` converts a duration string to a number of seconds.

Rules:

- Units are `d`, `h`, `m`, `s` (lowercase only).
- A duration is one or more `<integer><unit>` components written without spaces,
  for example `90s`, `1h30m`, `2d4h10s`.
- Components must appear in descending unit order (d, h, m, s) and each unit may
  appear at most once. Otherwise `ValueError`.
- `0s` is valid. An empty string, a missing unit, an unknown unit, a negative or
  non-integer number, or any whitespace raises `ValueError`.

Examples:

| input     | seconds |
|-----------|---------|
| `90s`     | 90      |
| `1h30m`   | 5400    |
| `2d4h10s` | 187210  |
