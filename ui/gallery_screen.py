from PIL import Image, ImageDraw

from config import (
    LW,
    GALLERY_UI_BG,
    RECENTLY_DELETED_UI_BG,
    GALLERY_IMAGE_BOX,
    BLACK,
)

from gallery import load_gallery_image
from ui.common import render, DEFAULT_FONT


def center_text(draw, text, y, font, fill=BLACK):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (LW - text_width) // 2
    draw.text((x, y), text, fill=fill, font=font)


def right_text(draw, text, y, font, fill=BLACK, right_x=474):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = right_x - text_width
    draw.text((x, y), text, fill=fill, font=font)


def draw_gallery(photo_paths, gallery_index, deleted_mode=False):
    bg_path = RECENTLY_DELETED_UI_BG if deleted_mode else GALLERY_UI_BG
    image = Image.open(bg_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    title = "Recently Deleted" if deleted_mode else "Gallery"

    # These text labels are dynamic so you can keep your Figma placeholder text generic.
    draw.text((18, 8), "Back", fill=BLACK, font=DEFAULT_FONT)
    center_text(draw, title, 8, DEFAULT_FONT)

    if photo_paths:
        count_text = f"{gallery_index + 1}/{len(photo_paths)}"
    else:
        count_text = "0/0"

    right_text(draw, count_text, 8, DEFAULT_FONT)

    x1, y1, x2, y2 = GALLERY_IMAGE_BOX

    if not photo_paths:
        center_text(draw, "No Photos", 150, DEFAULT_FONT)
    else:
        photo, photo_path = load_gallery_image(photo_paths, gallery_index)
        photo.thumbnail((x2 - x1, y2 - y1))

        x = x1 + ((x2 - x1) - photo.width) // 2
        y = y1 + ((y2 - y1) - photo.height) // 2

        image.paste(photo, (x, y))

    render(image)