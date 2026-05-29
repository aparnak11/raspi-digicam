from PIL import Image, ImageDraw

from config import (
    LW,
    LH,
    BG,
    BLACK,
    WHITE,
    PINK,
    LIGHT_PINK,
    DARK_PINK,
    GRAY,
    CAPTURE_BOX,
    GALLERY_BOX,
    BACK_BOX,
    PREV_BOX,
    NEXT_BOX,
)

from display import show_on_lcd
from gallery import load_gallery_image


def draw_camera(frame=None, message="READY"):
    image = Image.new("RGB", (LW, LH), BG)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, LW, 36), fill=LIGHT_PINK)
    draw.text((14, 10), "APARNA'S DIGICAM", fill=BLACK)
    draw.text((LW - 62, 10), "64GB", fill=BLACK)

    vf_x1, vf_y1 = 92, 52
    vf_x2, vf_y2 = 388, 255

    if frame is not None:
        frame = frame.resize((vf_x2 - vf_x1, vf_y2 - vf_y1))
        image.paste(frame, (vf_x1, vf_y1))

    draw.rectangle((vf_x1, vf_y1, vf_x2, vf_y2), outline=PINK, width=3)
    draw.rectangle((220, 135, 260, 172), outline=GRAY, width=2)

    draw.rounded_rectangle(
        (12, 70, 76, 125),
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((22, 90), "MODE", fill=BLACK)

    draw.rounded_rectangle(
        GALLERY_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((18, 175), "GALL", fill=BLACK)

    draw.ellipse(CAPTURE_BOX, outline=DARK_PINK, width=5)
    draw.ellipse((420, 135, 450, 165), fill=PINK)
    draw.text((410, 190), "CAPTURE", fill=BLACK)

    draw.rectangle((0, LH - 32, LW, LH), fill=LIGHT_PINK)
    draw.text((18, LH - 22), message, fill=BLACK)
    draw.text((LW - 70, LH - 22), "PHOTO", fill=BLACK)

    show_on_lcd(image)


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
    draw.text((25, 13), "BACK", fill=BLACK)

    draw.text((190, 10), "GALLERY", fill=BLACK)

    if not photo_paths:
        draw.text((175, 150), "NO PHOTOS YET", fill=BLACK)
    else:
        photo, photo_path = load_gallery_image(photo_paths, gallery_index)

        x = (LW - photo.width) // 2
        y = 55
        image.paste(photo, (x, y))

        count_text = f"{gallery_index + 1}/{len(photo_paths)}"
        draw.text((LW - 55, 12), count_text, fill=BLACK)
        draw.text((120, LH - 24), photo_path.name, fill=BLACK)

    draw.rounded_rectangle(
        PREV_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((26, 152), "PREV", fill=BLACK)

    draw.rounded_rectangle(
        NEXT_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((417, 152), "NEXT", fill=BLACK)

    draw.rectangle((0, LH - 32, LW, LH), fill=LIGHT_PINK)
    draw.text((18, LH - 22), "USE PREV / NEXT / BACK", fill=BLACK)

    show_on_lcd(image)
