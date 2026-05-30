from pathlib import Path

PHOTOS_DIR = Path.home() / "Desktop" / "Projects" / "digicam" / "photos"
PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

LW, LH = 480, 320

BG = "#fffafc"
BLACK = "#111111"
WHITE = "#ffffff"
PINK = "#d96c93"
LIGHT_PINK = "#f4c2d7"
DARK_PINK = "#b84f74"
GRAY = "#888888"

CAPTURE_BOX = (405, 120, 465, 180)
GALLERY_BOX = (12, 155, 76, 210)
MODE_BOX = (12, 70, 76, 125)
FILTERS = ["NORMAL", "B&W", "PINK", "GOLDEN"]

BACK_BOX = (12, 6, 82, 32)
PREV_BOX = (12, 130, 78, 190)
NEXT_BOX = (402, 130, 468, 190)
DELETE_BOX = (210, 290, 275, 315)
