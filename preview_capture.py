from picamera2 import Picamera2, Preview
from datetime import datetime
from pathlib import Path
import time

photos_dir = Path.home() / "Desktop" / "Projects" / "digicam" / "photos"
photos_dir.mkdir(exist_ok=True)

picam2 = Picamera2()

preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

picam2.start_preview(Preview.QTGL)
picam2.start()

print("Preview active...")
input("Press Enter to take a photo...")

filename = photos_dir / f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
picam2.capture_file(str(filename))

print(f"Saved: {filename}")

picam2.stop_preview()
picam2.stop()
