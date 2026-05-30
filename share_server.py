from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import threading
import os

from config import PHOTOS_DIR, TRANSFER_PORT

_server_started = False


def start_share_server():
    global _server_started

    if _server_started:
        return

    os.chdir(PHOTOS_DIR)

    server = ThreadingHTTPServer(("0.0.0.0", TRANSFER_PORT), SimpleHTTPRequestHandler)

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    _server_started = True

    print(f"Share server started on port {TRANSFER_PORT}")
