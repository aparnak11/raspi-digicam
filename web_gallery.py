from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

PHOTOS_DIR = Path.home() / "Desktop" / "Projects" / "digicam" / "photos"
PORT = 8000

os.chdir(PHOTOS_DIR)

server = ThreadingHTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)

print(f"Serving photos from: {PHOTOS_DIR}")
print(f"Open on iPhone: http://raspberrypi.local:{PORT}")
print("Press Ctrl+C to stop.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStopping server...")
    server.server_close()
