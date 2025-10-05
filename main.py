import http.server
import socketserver
import os

# Define the port you want to run the server on
PORT = 8005
# Define the directory you want to serve files from
DIRECTORY = "web"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving files from '{DIRECTORY}' at http://localhost:{PORT}")
    # This will keep the server running until you stop it (e.g., with Ctrl+C)
    httpd.serve_forever()
