# client

Service clients built on `client/session.py`. See `client/inventory.py` for an
existing example.

`fetch_status(url, ca_file=None) -> dict` (in `client/status.py`)

- Sends an HTTPS GET to `url`, parses the JSON body and returns it as a dict
  (the status service returns e.g. `{"status": "ok", "version": "1.4.2"}`).
- `ca_file` is the CA bundle used to validate the server certificate.
- Errors from the network layer propagate unchanged.
- Follow the same pattern as `fetch_inventory`.

Local development: `dev_server.py` serves the status endpoint over HTTPS using
the dev certificate in `certs/`. The CA for it is `certs/ca.pem`.
