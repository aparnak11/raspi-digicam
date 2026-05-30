from PIL import Image, ImageDraw
from ui.common import render, TITLE_FONT, BIG_BUTTON_FONT, SMALL_BUTTON_FONT, BODY_FONT, SMALL_FONT

from config import LW, LH, BG, BLACK, PINK, LIGHT_PINK
from ui.common import render


def draw_splash(message="Loading..."):
    image = Image.new("RGB", (LW, LH), BG)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, LW, LH), fill=BG)

    draw.rounded_rectangle(
        (70, 75, 410, 245),
        radius=24,
        fill=LIGHT_PINK,
        outline=PINK,
        width=4,
    )

    draw.text((145, 130), "APARNA'S DIGICAM", fill=BLACK, font=TITLE_FONT)

    draw.text((200, 205), message, fill=BLACK, font=BODY_FONT)

    render(image)
