cd /workspace
cat > client/status.py <<'PY'
from client.net import http_get_json


def fetch_status(url, ca_file=None):
    return http_get_json(url)
PY
