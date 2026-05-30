from picamera2 import Picamera2
from PIL import Image
from datetime import datetime
import time

from config import PHOTOS_DIR

picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)
picam2.start()
time.sleep(1)


def get_frame():
    array = picam2.capture_array()
    return Image.fromarray(array).convert("RGB")


def capture_photo(image=None):
    filename = PHOTOS_DIR / f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"

    if image is not None:
        image.save(filename)
    else:
        picam2.capture_file(str(filename))

    print(f"Saved: {filename}")
    return filename


def stop_camera():
    picam2.stop()
