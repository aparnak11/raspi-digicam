from picamera2 import Picamera2
from datetime import datetime
from pathlib import Path
import time

photos_dir = Path.home() / "Desktop" / "Projects" / "digicam" / "photos"
photos_dir.mkdir(exist_ok=True)

picam2 = Picamera2()
picam2.start()
time.sleep(2)

filename = photos_dir / f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
picam2.capture_file(str(filename))

print(f"Saved: {filename}")
picam2.stop()
