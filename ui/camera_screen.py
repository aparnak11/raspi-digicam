from datetime import datetime
import shutil
from PIL import Image, ImageDraw

from config import (
    CAMERA_UI_BG,
    VIEWFINDER_BOX,
    BLACK,
)

from ui.common import render, BODY_FONT, SMALL_FONT, DEFAULT_FONT


def get_storage_text():
    usage = shutil.disk_usage("/")
    free_gb = usage.free / (1024 ** 3)
    return f"{free_gb:.0f} GB"


def draw_camera(frame=None, message="Ready", filter_name="Normal"):
    image = Image.open(CAMERA_UI_BG).convert("RGB")
    draw = ImageDraw.Draw(image)

    vf_x1, vf_y1, vf_x2, vf_y2 = VIEWFINDER_BOX

    if frame is not None:
        frame = frame.resize((vf_x2 - vf_x1, vf_y2 - vf_y1))
        image.paste(frame, (vf_x1, vf_y1))

    current_time = datetime.now().strftime("%I:%M %p").lstrip("0")
    storage_text = get_storage_text()

    draw.text((407, 8), current_time, fill=BLACK, font=DEFAULT_FONT)
    draw.text((8, 298), message, fill=BLACK, font=DEFAULT_FONT)
    draw.text((215, 298), filter_name.title(), fill=BLACK, font=DEFAULT_FONT)
    draw.text((434, 298), storage_text, fill=BLACK, font=DEFAULT_FONT)

    render(image)