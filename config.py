from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

CAMERA_UI_BG = PROJECT_ROOT / "assets" / "ui" / "camera_screen.png"
GALLERY_UI_BG = PROJECT_ROOT / "assets" / "ui" / "gallery_screen.png"
SPLASH_UI_BG = PROJECT_ROOT / "assets" / "ui" / "splash_screen.png"
RECENTLY_DELETED_UI_BG = PROJECT_ROOT / "assets" / "ui" / "recently_deleted_screen.png"

PHOTOS_DIR = Path.home() / "Desktop" / "Projects" / "digicam" / "photos"
PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

RECENTLY_DELETED_DIR = Path.home() / "Desktop" / "Projects" / "digicam" / "recently_deleted"
RECENTLY_DELETED_DIR.mkdir(parents=True, exist_ok=True)

LW, LH = 480, 320

BG = "#fffafc"
BLACK = "#111111"
WHITE = "#ffffff"
PINK = "#d96c93"
LIGHT_PINK = "#f4c2d7"
DARK_PINK = "#b84f74"
GRAY = "#888888"

VIEWFINDER_BOX = (64, 44, 415, 276)
FILTER_BOX = (8, 80, 56, 130)
MODE_BOX = FILTER_BOX

GALLERY_BOX = (8, 190, 56, 240)
CAPTURE_BOX = (415, 130, 475, 190)

FILTERS = ["NORMAL", "B&W", "PINK", "SUNSET"]


GALLERY_IMAGE_BOX = (65, 45, 415, 276)

BACK_BOX = (0, 0, 80, 30)
PREV_BOX = (8, 135, 56, 184)
NEXT_BOX = (424, 135, 472, 184)

GALLERY_IMAGE_BOX = (65, 45, 415, 276)

BACK_BOX = (0, 0, 80, 30)
PREV_BOX = (8, 135, 56, 184)
NEXT_BOX = (424, 135, 472, 184)

RECENTLY_DELETED_BOX = (0, 290, 140, 320)
DELETE_BOX = (220, 290, 260, 320)
SHARE_BOX = (430, 290, 480, 320)

RESTORE_BOX = (0, 290, 150, 320)
DELETE_FOREVER_BOX = (215, 290, 265, 320)

SHARE_UI_BG = PROJECT_ROOT / "assets" / "ui" / "share_screen.png"

SHARE_QR_BOX = (140, 60, 340, 260)
SHARE_BACK_BOX = (0, 0, 80, 30)

TRANSFER_URL = "http://192.168.4.1:8000"
TRANSFER_PORT = 8000