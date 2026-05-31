from PIL import Image, ImageDraw
from ui.common import render, DEFAULT_FONT

from config import LW, LH, BG, BLACK, PINK, LIGHT_PINK
from ui.common import render

from config import SPLASH_UI_BG


def draw_splash(message="Loading..."):
    image = Image.open(
        SPLASH_UI_BG
    ).convert("RGB")

    draw = ImageDraw.Draw(image)

    draw.text(
        (205, 190),
        message,
        fill="black",
        font=DEFAULT_FONT,
    )

    render(image)

def draw_shutdown_splash(message="Goodbye!"):
    draw_splash(message)
