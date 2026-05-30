import qrcode
from PIL import Image, ImageDraw

from config import LW, LH, BG, BLACK, PINK, LIGHT_PINK
from ui.common import render

url = "http://192.168.4.1:8000"

qr = qrcode.make(url).convert("RGB")
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

draw.text((145, 285), url, fill=BLACK)

render(image)

input("Press Enter to exit...")
