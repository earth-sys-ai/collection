from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps
from collect import handle

# handler class
class RequestHandler(BaseHTTPRequestHandler):

    # cors header
    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

    # send dict
    def send_dict_response(self, d):
        self.wfile.write(bytes(dumps(d), "utf8"))

    # send options
    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    # where the magic happens
    def do_POST(self):
        self.send_response(200)
        self._send_cors_headers()
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        dataLength = int(self.headers["Content-Length"])
        data = self.rfile.read(dataLength)

        handle(data)

        response = {}
        response["status"] = "OK"
        self.send_dict_response(response)

# init
print("Starting server")
httpd = HTTPServer(("127.0.0.1", 8001), RequestHandler)
print("Hosting server on port 8001")
httpd.serve_forever()
