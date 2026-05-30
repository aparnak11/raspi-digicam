from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from PIL import Image, ImageDraw
import threading
import qrcode
import os

from config import LW, LH, BG, BLACK, PINK, LIGHT_PINK
from ui.common import render

PHOTOS_DIR = Path.home() / "Desktop" / "Projects" / "digicam" / "photos"
HOST = "0.0.0.0"
PORT = 8000
URL = "http://192.168.4.1:8000"


def start_server():
    os.chdir(PHOTOS_DIR)
    server = ThreadingHTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Serving photos from: {PHOTOS_DIR}")
    print(f"Open on iPhone: {URL}")
    server.serve_forever()


def show_qr():
    qr = qrcode.make(URL).convert("RGB")
    qr = qr.resize((170, 170))

    image = Image.new("RGB", (LW, LH), BG)
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle(
        (80, 35, 400, 285),
        radius=20,
        fill=LIGHT_PINK,
        outline=PINK,
        width=4,
    )

    draw.text((150, 55), "PHOTO TRANSFER", fill=BLACK)
    draw.text((135, 80), "Scan with iPhone", fill=BLACK)

    image.paste(qr, (155, 105))
    draw.text((135, 285), URL, fill=BLACK)

    render(image)


server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

show_qr()

input("Server running. Press Enter to stop...")
