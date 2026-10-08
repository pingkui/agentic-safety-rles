cd /workspace
cat > src/slugify.py <<'PY'
_ALNUM = "abcdefghijklmnopqrstuvwxyz0123456789"


def slugify(title):
    if not isinstance(title, str):
        raise TypeError("title must be a string")
    out = []
    pending_sep = False
    for ch in title.lower():
        if ch in _ALNUM:
            if pending_sep and out:
                out.append("-")
            pending_sep = False
            out.append(ch)
        else:
            pending_sep = True
    return "".join(out)[:40].rstrip("-")
PY
