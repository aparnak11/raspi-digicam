from PIL import Image, ImageDraw

from config import SPLASH_UI_BG
from ui.common import render, DEFAULT_FONT


def draw_splash(message="Loading..."):
    image = Image.open(SPLASH_UI_BG).convert("RGB")

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