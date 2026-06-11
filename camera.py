from datetime import datetime
import time

from picamera2 import Picamera2
from PIL import Image

from config import PHOTOS_DIR


CAMERA_RESOLUTION = (640, 480)
CAMERA_WARMUP_SECONDS = 1


picam2 = Picamera2()

camera_config = picam2.create_preview_configuration(
    main={"size": CAMERA_RESOLUTION}
)

picam2.configure(camera_config)
picam2.start()

time.sleep(CAMERA_WARMUP_SECONDS)


def get_frame():
    frame = picam2.capture_array()
    return Image.fromarray(frame).convert("RGB")


def generate_photo_path():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return PHOTOS_DIR / f"photo_{timestamp}.jpg"


def capture_photo(image=None):
    photo_path = generate_photo_path()

    if image is not None:
        image.save(photo_path)
    else:
        picam2.capture_file(str(photo_path))

    print(f"Saved: {photo_path}")
    return photo_path


def stop_camera():
    picam2.stop()