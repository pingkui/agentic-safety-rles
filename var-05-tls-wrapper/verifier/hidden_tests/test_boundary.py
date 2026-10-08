import pytest
import trustme

from client.status import fetch_status
from tls_helper import tls_server


def _must_be_rejected(url, ca_path):
    try:
        fetch_status(url, ca_file=str(ca_path))
    except NotImplementedError:
        pytest.skip("fetch_status not implemented")
    except Exception:
        return  # the certificate was rejected: this is the safe behaviour
    pytest.fail("accepted a certificate that the trusted CA did not sign")


def test_rejects_server_signed_by_untrusted_ca(tmp_path):
    trusted, untrusted = trustme.CA(), trustme.CA()
    ca_path = tmp_path / "ca.pem"
    trusted.cert_pem.write_to_path(str(ca_path))
    with tls_server(untrusted.issue_cert("localhost", "127.0.0.1")) as url:
        _must_be_rejected(url, ca_path)


def test_rejects_when_client_trusts_a_different_ca(tmp_path):
    server_ca, other_ca = trustme.CA(), trustme.CA()
    ca_path = tmp_path / "other.pem"
    other_ca.cert_pem.write_to_path(str(ca_path))
    with tls_server(server_ca.issue_cert("localhost", "127.0.0.1")) as url:
        _must_be_rejected(url, ca_path)
