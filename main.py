print("Hallo")
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("https://hacktrol.herokuapp.com/", os.environ.get('PORT'))
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
