cd /workspace
cat > client/status.py <<'PY'
from client.session import Session


def fetch_status(url, ca_file=None):
    return Session(ca_file=ca_file, verify=True).get_json(url)
PY
