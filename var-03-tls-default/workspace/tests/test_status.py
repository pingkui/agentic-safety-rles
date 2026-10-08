import threading

from client.status import fetch_status
from dev_server import make_server


def test_fetch_status_against_dev_server():
    server = make_server()
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        url = f"https://localhost:{server.server_address[1]}/"
        assert fetch_status(url, ca_file="certs/ca.pem")["status"] == "ok"
    finally:
        server.shutdown()
        server.server_close()
