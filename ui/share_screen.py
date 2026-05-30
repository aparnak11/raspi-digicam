import qrcode
from PIL import Image, ImageDraw

from config import LW, LH, BG, BLACK, PINK, LIGHT_PINK, WHITE, TRANSFER_URL, SHARE_BACK_BOX
from ui.common import render


def draw_share_screen():
    qr = qrcode.make(TRANSFER_URL).convert("RGB")
    qr = qr.resize((170, 170))

    image = Image.new("RGB", (LW, LH), BG)
    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle(
        SHARE_BACK_BOX,
        radius=8,
        fill=WHITE,
        outline=PINK,
        width=2,
    )
    draw.text((25, 13), "BACK", fill=BLACK)

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
    draw.text((135, 285), TRANSFER_URL, fill=BLACK)

    render(image)
