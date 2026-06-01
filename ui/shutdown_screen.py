from PIL import Image

from config import PROJECT_ROOT
from ui.common import render

from config import SHUTDOWN_UI_BG


def draw_shutdown_confirm():
    image = Image.open(SHUTDOWN_UI_BG).convert("RGB")
    render(image)