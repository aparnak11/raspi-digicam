from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
from pathlib import Path
import threading

from config import PHOTOS_DIR, TRANSFER_PORT

_server_started = False


class PhotoShareHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.show_gallery()
            return

        if self.path.startswith("/photo/"):
            filename = unquote(self.path.replace("/photo/", ""))
            photo_path = PHOTOS_DIR / filename

            if photo_path.exists() and photo_path.suffix.lower() in [".jpg", ".jpeg", ".png"]:
                self.send_response(200)
                self.send_header("Content-Type", "image/jpeg")
                self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
                self.end_headers()

                with open(photo_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404)

            return

        self.send_error(404)

    def show_gallery(self):
        photos = sorted(PHOTOS_DIR.glob("*.jpg"), key=lambda p: p.stat().st_mtime, reverse=True)

        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Aparna's Digicam</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: #fffafc;
                    color: #111;
                }

                header {
                    background: #f4c2d7;
                    padding: 16px;
                    text-align: center;
                    font-weight: bold;
                    font-size: 22px;
                }

                .subheader {
                    padding: 10px;
                    text-align: center;
                    font-size: 14px;
                }

                .grid {
                    display: grid;
                    grid-template-columns: repeat(2, 1fr);
                    gap: 12px;
                    padding: 12px;
                }

                .photo-card {
                    background: white;
                    border: 2px solid #d96c93;
                    border-radius: 14px;
                    padding: 8px;
                    text-align: center;
                }

                img {
                    width: 100%;
                    aspect-ratio: 1 / 1;
                    object-fit: cover;
                    border-radius: 10px;
                }

                a {
                    display: block;
                    margin-top: 8px;
                    color: #111;
                    font-weight: bold;
                    text-decoration: none;
                }

                .filename {
                    font-size: 11px;
                    word-break: break-word;
                    opacity: 0.7;
                }
            </style>
        </head>
        <body>
            <header>Aparna's Digicam</header>
            <div class="subheader">Tap a photo to download it to your phone</div>
            <div class="grid">
        """

        for photo in photos:
            url = f"/photo/{photo.name}"
            html += f"""
                <div class="photo-card">
                    <a href="{url}">
                        <img src="{url}">
                    </a>
                </div>
            """

        html += """
            </div>
        </body>
        </html>
        """

        encoded = html.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


def start_share_server():
    global _server_started

    if _server_started:
        return

    server = ThreadingHTTPServer(("0.0.0.0", TRANSFER_PORT), PhotoShareHandler)

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    _server_started = True

    print(f"Share server started on port {TRANSFER_PORT}")