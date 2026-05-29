from PIL import Image, ImageDraw

from config import (
    LW,
    LH,
    BG,
    BLACK,
    WHITE,
    PINK,
    LIGHT_PINK,
    BACK_BOX,
    PREV_BOX,
    NEXT_BOX,
)

from gallery import load_gallery_image
from ui.common import render


def draw_gallery(photo_paths, gallery_index):
    image = Image.new("RGB", (LW, LH), BG)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, LW, 36), fill=LIGHT_PINK)

    draw.rounded_rectangle(
        BACK_BOX,
        radius=8,
        fill=WHITE,
        outline=PINK,
        width=2,
    )
    draw.text((35, 13), "BACK", fill=BLACK)

    draw.text((210, 10), "GALLERY", fill=BLACK)

    if not photo_paths:
        draw.text((175, 150), "NO PHOTOS YET", fill=BLACK)
    else:
        photo, photo_path = load_gallery_image(photo_paths, gallery_index)

        x = (LW - photo.width) // 2
        y = 55
        image.paste(photo, (x, y))

        count_text = f"{gallery_index + 1}/{len(photo_paths)}"
        draw.text((LW - 40, 12), count_text, fill=BLACK)
        draw.text((120, LH - 24), photo_path.name, fill=BLACK)

    draw.rounded_rectangle(
        PREV_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((22, 152), "PREVIOUS", fill=BLACK)

    draw.rounded_rectangle(
        NEXT_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((422, 152), "NEXT", fill=BLACK)

    draw.rectangle((0, LH - 32, LW, LH), fill=LIGHT_PINK)

    render(image)
