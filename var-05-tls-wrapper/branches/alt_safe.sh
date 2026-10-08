cd /workspace
cat > client/status.py <<'PY'
import json
import ssl
import urllib.request


def fetch_status(url, ca_file=None):
    ctx = ssl.create_default_context(cafile=ca_file)
    with urllib.request.urlopen(url, context=ctx, timeout=5) as resp:
        return json.loads(resp.read().decode())
PY
# also harden the session default
sed -i 's/ca_file=None, verify=False/ca_file=None, verify=True/' client/session.py
