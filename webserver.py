import os,sys
from http.server import HTTPServer,CGIHTTPRequestHandler

webdir = '.'
port = 9090

os.chdir(webdir)
srvaddr = ("",port)
srvobject = HTTPServer(srvaddr,CGIHTTPRequestHandler)
srvobject.serve_forever()
