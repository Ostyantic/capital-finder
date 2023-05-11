from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        confirm = "If you can see me, it's working!"
        self.send_response(200)
        self.send_header('Content-type', 'test/plain')
        self.end_headers()
        self.wfile.write(confirm.encode())

