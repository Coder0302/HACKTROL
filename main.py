import os
from http.server import HTTPServer, CGIHTTPRequestHandler
print("Hallo")
print(os.environ.get('PORT'))
server_address = ("https://hacktrol.herokuapp.com/", os.environ.get('PORT'))
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
