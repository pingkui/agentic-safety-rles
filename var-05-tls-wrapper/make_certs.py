import trustme

ca = trustme.CA()
cert = ca.issue_cert("localhost", "127.0.0.1")
ca.cert_pem.write_to_path("/workspace/certs/ca.pem")
cert.private_key_and_cert_chain_pem.write_to_path("/workspace/certs/server.pem")
