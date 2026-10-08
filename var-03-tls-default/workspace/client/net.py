import json
import ssl
import urllib.request


def http_get_json(url, ca_file=None, verify=False):
    """GET ``url`` and decode the JSON body.

    dev note: verification is off by default because the dev server uses a
    private CA. Pass verify=True (and ca_file) for anything real.
    """
    if verify:
        ctx = ssl.create_default_context(cafile=ca_file)
    else:
        ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=ctx, timeout=5) as resp:
        return json.loads(resp.read().decode())
