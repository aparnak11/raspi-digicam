from PIL import Image, ImageDraw
from ui.common import render, TITLE_FONT, BUTTON_FONT, BODY_FONT, SMALL_FONT

from config import (
    LW,
    LH,
    BG,
    BLACK,
    PINK,
    LIGHT_PINK,
    DARK_PINK,
    GRAY,
    CAPTURE_BOX,
    GALLERY_BOX,
    MODE_BOX,
)

from ui.common import render


def draw_camera(frame=None, message="READY", filter_name="NORMAL"):
    image = Image.new("RGB", (LW, LH), BG)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, LW, 36), fill=LIGHT_PINK)
    draw.text((14, 10), "APARNA'S DIGICAM", fill=BLACK, font=TITLE_FONT)
    draw.text((LW - 37, 10), "64GB", fill=BLACK, font=SMALL_FONT)

    vf_x1, vf_y1 = 85, 45
    vf_x2, vf_y2 = 398, 278

    if frame is not None:
        frame = frame.resize((vf_x2 - vf_x1, vf_y2 - vf_y1))
        image.paste(frame, (vf_x1, vf_y1))

    draw.rectangle((vf_x1, vf_y1, vf_x2, vf_y2), outline=PINK, width=3)
    draw.rectangle((220, 135, 260, 172), outline=GRAY, width=2)

    draw.rounded_rectangle(
        GALLERY_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((23, 175), "GALLERY", fill=BLACK, font=BUTTON_FONT)

    draw.ellipse(CAPTURE_BOX, outline=DARK_PINK, width=5)
    draw.ellipse((420, 135, 450, 165), fill=PINK)

    draw.rectangle((0, LH - 32, LW, LH), fill=LIGHT_PINK)
    draw.text((14, LH - 22), message, fill=BLACK, font=BODY_FONT)
    draw.text((LW - 45, LH - 22), "PHOTO", fill=BLACK, font=BODY_FONT)

    draw.rounded_rectangle(
        MODE_BOX,
        radius=12,
        fill=LIGHT_PINK,
        outline=PINK,
        width=2,
    )
    draw.text((25, 85), "MODE", fill=BLACK, font=BUTTON_FONT)
    draw.text((LW/2, LH - 22), filter_name, fill=BLACK, font=BODY_FONT)

    render(image)
