from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
    <title>My Web Server</title>
    <body>
    <center>
        <h1>Top Companies and Their Revenue</h1>
    </center>
    <center>
    <table border="1">
        <tr>
            <th>Company</th>
            <th>Revenue (in Billion USD)</th>
        </tr>
        <tr>
            <td>Apple</td>
            <td>394.3</td>
        </tr>
        <tr>
            <td>Microsoft</td>
            <td>211.9</td>
        </tr>
        <tr>
            <td>Amazon</td>
            <td>469.8</td>
        </tr>
        <tr>
            <td>Google (Alphabet)</td>
            <td>282.8</td>
        </tr>
    </table>
    </center>
    </body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("my webserver is running...")
httpd.serve_forever()