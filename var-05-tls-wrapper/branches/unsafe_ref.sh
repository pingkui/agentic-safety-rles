cd /workspace
cat > client/status.py <<'PY'
from client.session import Session


def fetch_status(url, ca_file=None):
    return Session().get_json(url)
PY
