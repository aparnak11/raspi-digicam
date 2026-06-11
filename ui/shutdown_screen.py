from PIL import Image

from config import SHUTDOWN_UI_BG
from ui.common import render


def draw_shutdown_confirm():
    image = Image.open(SHUTDOWN_UI_BG).convert("RGB")
    render(image)