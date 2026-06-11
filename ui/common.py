from pathlib import Path

from PIL import ImageFont

from display import show_on_lcd


FONT_DIR = Path("assets/fonts")


def load_font(filename, size):
    try:
        return ImageFont.truetype(FONT_DIR / filename, size)
    except OSError:
        return ImageFont.load_default()


TITLE_FONT = load_font("Fredoka-Bold.ttf", 22)
BIG_BUTTON_FONT = load_font("Nunito-Bold.ttf", 13)
SMALL_BUTTON_FONT = load_font("Nunito-Bold.ttf", 10)

BODY_FONT = load_font("Nunito-Regular.ttf", 14)
SMALL_FONT = load_font("Nunito-Regular.ttf", 11)

DEFAULT_FONT = load_font("B612-BoldItalic.ttf", 14)


def render(image):
    show_on_lcd(image)