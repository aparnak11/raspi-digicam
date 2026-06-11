import qrcode
from PIL import Image, ImageDraw

from config import SHARE_UI_BG, SHARE_QR_BOX, TRANSFER_URL, BLACK
from ui.common import render, DEFAULT_FONT


def draw_share_screen():
    image = Image.open(SHARE_UI_BG).convert("RGB")
    draw = ImageDraw.Draw(image)

    qr_x1, qr_y1, qr_x2, qr_y2 = SHARE_QR_BOX
    qr_size = min(qr_x2 - qr_x1, qr_y2 - qr_y1)

    qr = qrcode.make(TRANSFER_URL).convert("RGB")
    qr = qr.resize((qr_size, qr_size))

    image.paste(qr, (qr_x1, qr_y1))

    draw.text((300, 297), TRANSFER_URL, fill=BLACK, font=DEFAULT_FONT)

    render(image)