import http.server
import json
import ssl


def make_server(port=0, certfile="certs/server.pem"):
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            body = json.dumps({"status": "ok", "version": "1.4.2"}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = http.server.HTTPServer(("127.0.0.1", port), Handler)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(certfile)
    server.socket = ctx.wrap_socket(server.socket, server_side=True)
    return server


if __name__ == "__main__":
    srv = make_server(8443)
    print("serving on https://localhost:8443/")
    srv.serve_forever()
