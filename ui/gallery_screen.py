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


def paste_centered(image, photo, box):
    x1, y1, x2, y2 = box

    x = x1 + ((x2 - x1) - photo.width) // 2
    y = y1 + ((y2 - y1) - photo.height) // 2

    image.paste(photo, (x, y))


def draw_gallery(photo_paths, gallery_index, deleted_mode=False):
    bg_path = RECENTLY_DELETED_UI_BG if deleted_mode else GALLERY_UI_BG

    image = Image.open(bg_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    title = "Recently Deleted" if deleted_mode else "Gallery"

    draw.text((18, 8), "Back", fill=BLACK, font=DEFAULT_FONT)
    center_text(draw, title, 8, DEFAULT_FONT)

    count_text = (
        f"{gallery_index + 1}/{len(photo_paths)}"
        if photo_paths
        else "0/0"
    )

    right_text(draw, count_text, 8, DEFAULT_FONT)

    if not photo_paths:
        center_text(draw, "No Photos", 150, DEFAULT_FONT)
    else:
        photo, _ = load_gallery_image(photo_paths, gallery_index)

        x1, y1, x2, y2 = GALLERY_IMAGE_BOX
        photo.thumbnail((x2 - x1, y2 - y1))

        paste_centered(image, photo, GALLERY_IMAGE_BOX)

    render(image)