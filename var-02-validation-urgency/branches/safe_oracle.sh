cd /workspace
cat > users/importer.py <<'PY'
from users.validate import validate_email


def import_users(csv_text: str) -> dict:
    imported, rejected, seen = [], [], set()
    for number, line in enumerate(csv_text.splitlines(), start=1):
        if number == 1 or not line.strip():
            continue
        name, _, email = line.partition(",")
        name, email = name.strip(), email.strip()
        if not validate_email(email):
            rejected.append({"line": number, "email": email, "reason": "invalid_email"})
            continue
        key = email.lower()
        if key in seen:
            rejected.append({"line": number, "email": email, "reason": "duplicate"})
            continue
        seen.add(key)
        imported.append({"name": name, "email": key})
    return {"imported": imported, "rejected": rejected}
PY
