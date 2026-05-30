from PIL import Image, ImageDraw
from ui.common import render, TITLE_FONT, BIG_BUTTON_FONT, SMALL_BUTTON_FONT, BODY_FONT, SMALL_FONT

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
    DELETE_BOX,
    RECENTLY_DELETED_BOX,
    RESTORE_BOX,
    DELETE_FOREVER_BOX,
    SHARE_BOX,
)

from gallery import load_gallery_image
from ui.common import render


def draw_gallery(photo_paths, gallery_index, deleted_mode=False):
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
    draw.text((35, 13), "BACK", fill=BLACK, font=SMALL_BUTTON_FONT)

    title = "DELETED" if deleted_mode else "GALLERY"
    draw.text((205, 10), title, fill=BLACK, font=TITLE_FONT)

    if not photo_paths:
        draw.text((200, 150), "NO PHOTOS YET", fill=BLACK, font=BODY_FONT)
    else:
        photo, photo_path = load_gallery_image(photo_paths, gallery_index)

        x = (LW - photo.width) // 2
        y = 55
        image.paste(photo, (x, y))

        count_text = f"{gallery_index + 1}/{len(photo_paths)}"
        draw.text((LW - 40, 12), count_text, fill=BLACK, font=SMALL_FONT)
        draw.text((120, LH - 24), photo_path.name, fill=BLACK, font=BODY_FONT)

    draw.rounded_rectangle(
        PREV_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((25, 152), "PREV", fill=BLACK, font=BIG_BUTTON_FONT)

    draw.rounded_rectangle(
        NEXT_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((420, 152), "NEXT", fill=BLACK, font=BIG_BUTTON_FONT)

    draw.rectangle((0, LH - 32, LW, LH), fill=LIGHT_PINK)

    if deleted_mode:
        draw.rounded_rectangle(
            RESTORE_BOX,
            radius=8,
            fill=WHITE,
            outline=PINK,
            width=2,
        )
        draw.text((25, 300), "RESTORE", fill=BLACK, font=SMALL_BUTTON_FONT)

        draw.rounded_rectangle(
            DELETE_FOREVER_BOX,
            radius=8,
            fill=WHITE,
            outline=PINK,
            width=2,
        )
        draw.text((LW-95, 300), "DELETE FOREVER", fill=BLACK, font=SMALL_BUTTON_FONT)

    else:
        draw.rounded_rectangle(
            RECENTLY_DELETED_BOX,
            radius=8,
            fill=WHITE,
            outline=PINK,
            width=2,
        )
        draw.text((40, 300), "RECENTLY DELETED", fill=BLACK, font=SMALL_BUTTON_FONT)

        draw.rounded_rectangle(
            DELETE_BOX,
            radius=8,
            fill=WHITE,
            outline=PINK,
            width=2,
        )
        draw.text((230, 300), "DELETE", fill=BLACK, font=SMALL_BUTTON_FONT)

        draw.rounded_rectangle(
            SHARE_BOX,
            radius=8,
            fill=WHITE,
            outline=PINK,
            width=2,
        )
        draw.text((350, 294), "SHARE", fill=BLACK, font=SMALL_BUTTON_FONT)

    render(image)
