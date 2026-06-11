from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os


PHOTOS_DIR = Path.home() / "Desktop" / "Projects" / "digicam" / "photos"
HOST = "0.0.0.0"
PORT = 8000


def main():
    os.chdir(PHOTOS_DIR)

    server = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

    print(f"Serving photos from: {PHOTOS_DIR}")
    print(f"Open on iPhone: http://raspberrypi.local:{PORT}")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()


if __name__ == "__main__":
    main()