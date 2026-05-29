from PIL import Image, ImageDraw
from picamera2 import Picamera2
from pathlib import Path
from datetime import datetime
import st7796
import ft6336u
import time

# ---------- Paths ----------
photos_dir = Path.home() / "Desktop" / "Projects" / "digicam" / "photos"
photos_dir.mkdir(parents=True, exist_ok=True)

# ---------- LCD ----------
lcd = st7796.st7796()
lcd.lcd_init()
lcd.clear()

# ---------- Touchscreen ----------
tp = ft6336u.ft6336u()

# ---------- Camera ----------
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)
picam2.start()
time.sleep(1)

# ---------- Colors ----------
bg = "#fffafc"
black = "#111111"
white = "#ffffff"
pink = "#d96c93"
light_pink = "#f4c2d7"
dark_pink = "#b84f74"
gray = "#888888"

LW, LH = 480, 320


def show_on_lcd(image):
    image = image.rotate(90, expand=True)
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    lcd.show_image(image)


def touch_to_landscape(x, y):
    lx = 480 - y
    ly = 320 - x
    return lx, ly


def in_box(lx, ly, box):
    x1, y1, x2, y2 = box
    return x1 <= lx <= x2 and y1 <= ly <= y2


CAPTURE_BOX = (405, 120, 465, 180)
GALLERY_BOX = (12, 155, 76, 210)

BACK_BOX = (12, 6, 82, 32)
PREV_BOX = (12, 130, 78, 190)
NEXT_BOX = (402, 130, 468, 190)


def draw_camera(frame=None, message="READY"):
    image = Image.new("RGB", (LW, LH), bg)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, LW, 36), fill=light_pink)
    draw.text((14, 10), "APARNA'S DIGICAM", fill=black)
    draw.text((LW - 62, 10), "64GB", fill=black)

    vf_x1, vf_y1 = 92, 52
    vf_x2, vf_y2 = 388, 255

    if frame is not None:
        frame = frame.resize((vf_x2 - vf_x1, vf_y2 - vf_y1))
        image.paste(frame, (vf_x1, vf_y1))

    draw.rectangle((vf_x1, vf_y1, vf_x2, vf_y2), outline=pink, width=3)
    draw.rectangle((220, 135, 260, 172), outline=gray, width=2)

    draw.rounded_rectangle(
        (12, 70, 76, 125),
        radius=12,
        fill=light_pink,
        outline=pink,
        width=2,
    )
    draw.text((22, 90), "MODE", fill=black)

    draw.rounded_rectangle(
        GALLERY_BOX,
        radius=12,
        fill=light_pink,
        outline=pink,
        width=2,
    )
    draw.text((18, 175), "GALL", fill=black)

    draw.ellipse(CAPTURE_BOX, outline=dark_pink, width=5)
    draw.ellipse((420, 135, 450, 165), fill=pink)
    draw.text((410, 190), "CAPTURE", fill=black)

    draw.rectangle((0, LH - 32, LW, LH), fill=light_pink)
    draw.text((18, LH - 22), message, fill=black)
    draw.text((LW - 70, LH - 22), "PHOTO", fill=black)

    show_on_lcd(image)


def draw_gallery(photo_paths, gallery_index):
    image = Image.new("RGB", (LW, LH), bg)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, LW, 36), fill=light_pink)

    draw.rounded_rectangle(
        BACK_BOX,
        radius=8,
        fill=white,
        outline=pink,
        width=2,
    )
    draw.text((25, 13), "BACK", fill=black)

    draw.text((190, 10), "GALLERY", fill=black)

    if not photo_paths:
        draw.text((175, 150), "NO PHOTOS YET", fill=black)
    else:
        photo_path = photo_paths[gallery_index]
        photo = Image.open(photo_path).convert("RGB")
        photo.thumbnail((300, 220))

        x = (LW - photo.width) // 2
        y = 55
        image.paste(photo, (x, y))

        count_text = f"{gallery_index + 1}/{len(photo_paths)}"
        draw.text((LW - 55, 12), count_text, fill=black)
        draw.text((120, LH - 24), photo_path.name, fill=black)

    draw.rounded_rectangle(
        PREV_BOX,
        radius=12,
        fill=light_pink,
        outline=pink,
        width=2,
    )
    draw.text((26, 152), "PREV", fill=black)

    draw.rounded_rectangle(
        NEXT_BOX,
        radius=12,
        fill=light_pink,
        outline=pink,
        width=2,
    )
    draw.text((417, 152), "NEXT", fill=black)

    draw.rectangle((0, LH - 32, LW, LH), fill=light_pink)
    draw.text((18, LH - 22), "USE PREV / NEXT / BACK", fill=black)

    show_on_lcd(image)


def capture_photo():
    filename = photos_dir / f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    picam2.capture_file(str(filename))
    print(f"Saved: {filename}")
    return filename


def get_photos():
    return sorted(photos_dir.glob("*.jpg"), key=lambda p: p.stat().st_mtime)


def get_touch():
    tp.read_touch_data()
    point_count, coords = tp.get_touch_xy()

    if point_count > 0:
        raw_x = coords[0]["x"]
        raw_y = coords[0]["y"]
        lx, ly = touch_to_landscape(raw_x, raw_y)
        return lx, ly

    return None


try:
    mode = "camera"
    photo_paths = get_photos()
    gallery_index = max(0, len(photo_paths) - 1)

    while True:
        touch = get_touch()

        if mode == "camera":
            array = picam2.capture_array()
            frame = Image.fromarray(array).convert("RGB")

            draw_camera(frame, "READY")

            if touch:
                lx, ly = touch
                print(f"touch landscape: x={lx}, y={ly}")

                if in_box(lx, ly, CAPTURE_BOX):
                    draw_camera(frame, "SAVING...")
                    filename = capture_photo()
                    draw_camera(frame, "SAVED!")
                    time.sleep(1)

                    photo_paths = get_photos()
                    gallery_index = max(0, len(photo_paths) - 1)

                elif in_box(lx, ly, GALLERY_BOX):
                    photo_paths = get_photos()
                    gallery_index = max(0, len(photo_paths) - 1)
                    mode = "gallery"
                    draw_gallery(photo_paths, gallery_index)
                    time.sleep(0.5)

        elif mode == "gallery":
            if touch:
                lx, ly = touch
                print(f"gallery touch: x={lx}, y={ly}")

                if in_box(lx, ly, BACK_BOX):
                    mode = "camera"
                    time.sleep(0.5)

                elif in_box(lx, ly, PREV_BOX):
                    if photo_paths:
                        gallery_index = max(0, gallery_index - 1)
                        draw_gallery(photo_paths, gallery_index)
                    time.sleep(0.35)

                elif in_box(lx, ly, NEXT_BOX):
                    if photo_paths:
                        gallery_index = min(len(photo_paths) - 1, gallery_index + 1)
                        draw_gallery(photo_paths, gallery_index)
                    time.sleep(0.35)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    picam2.stop()
    lcd.clear()
