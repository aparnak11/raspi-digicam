from PIL import Image, ImageDraw

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
)

from ui.common import render


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

    render(image)
