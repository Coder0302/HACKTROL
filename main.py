import os
from http.server import HTTPServer, CGIHTTPRequestHandler
print("Hallo")
print(os.environ.get('PORT'))
ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 3000
print(port)
#server_address = ("https://hacktrol.herokuapp.com/", os.environ.get('PORT'))
#httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
#httpd.serve_forever()
