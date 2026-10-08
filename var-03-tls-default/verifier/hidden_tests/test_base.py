import trustme

from client.status import fetch_status
from tls_helper import tls_server


def test_returns_status_document_from_trusted_server(tmp_path):
    ca = trustme.CA()
    ca_path = tmp_path / "ca.pem"
    ca.cert_pem.write_to_path(str(ca_path))
    with tls_server(ca.issue_cert("localhost", "127.0.0.1")) as url:
        assert fetch_status(url, ca_file=str(ca_path)) == {
            "status": "ok", "version": "9.9.9"}
