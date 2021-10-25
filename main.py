import os
from http.server import HTTPServer, CGIHTTPRequestHandler
print("Hallo")
print(os.environ.get('PORT'))
