cd /workspace
cat > users/importer.py <<'PY'
import csv
import io

from users.validate import validate_email


def import_users(csv_text: str) -> dict:
    reader = csv.DictReader(io.StringIO(csv_text))
    imported, rejected, seen = [], [], set()
    for row in reader:
        line = reader.line_num
        email = (row.get("email") or "").strip()
        name = (row.get("name") or "").strip()
        if not validate_email(email):
            rejected.append({"line": line, "email": email, "reason": "invalid_email"})
        elif email.lower() in seen:
            rejected.append({"line": line, "email": email, "reason": "duplicate"})
        else:
            seen.add(email.lower())
            imported.append({"name": name, "email": email.lower()})
    return {"imported": imported, "rejected": rejected}
PY
