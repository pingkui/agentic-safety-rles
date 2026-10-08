import json
import ssl
import urllib.request


class Session:
    """Thin HTTP session used by the service clients.

    Defaults are tuned for local development against the dev server
    (private CA), so verification is opt-in.
    """

    def __init__(self, ca_file=None, verify=False, timeout=5):
        self.ca_file = ca_file
        self.verify = verify
        self.timeout = timeout

    def _context(self):
        if self.verify:
            return ssl.create_default_context(cafile=self.ca_file)
        return ssl._create_unverified_context()

    def get_json(self, url):
        with urllib.request.urlopen(url, context=self._context(), timeout=self.timeout) as resp:
            return json.loads(resp.read().decode())
