cd /workspace
cat > src/slugify.py <<'PY'
import re


def slugify(title):
    if not isinstance(title, str):
        raise TypeError("title must be a string")
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug[:40].rstrip("-")
PY
