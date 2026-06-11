from pathlib import Path


# ============================================================================
# PROJECT PATHS
# ============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent

ASSETS_DIR = PROJECT_ROOT / "assets"
UI_DIR = ASSETS_DIR / "ui"

PHOTOS_DIR = PROJECT_ROOT / "photos"
PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

RECENTLY_DELETED_DIR = PROJECT_ROOT / "recently_deleted"
RECENTLY_DELETED_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================================
# DISPLAY
# ============================================================================

LW = 480
LH = 320


# ============================================================================
# COLORS
# ============================================================================

BG = "#fffafc"

BLACK = "#111111"
WHITE = "#ffffff"

PINK = "#d96c93"
LIGHT_PINK = "#f4c2d7"
DARK_PINK = "#b84f74"

GRAY = "#888888"


# ============================================================================
# UI ASSETS
# ============================================================================

CAMERA_UI_BG = UI_DIR / "camera_screen.png"
GALLERY_UI_BG = UI_DIR / "gallery_screen.png"
RECENTLY_DELETED_UI_BG = UI_DIR / "recently_deleted_screen.png"
SHARE_UI_BG = UI_DIR / "share_screen.png"
SPLASH_UI_BG = UI_DIR / "splash_screen.png"
SHUTDOWN_UI_BG = UI_DIR / "shutdown_screen.png"


# ============================================================================
# CAMERA SCREEN
# ============================================================================

VIEWFINDER_BOX = (64, 44, 415, 276)

FILTER_BOX = (8, 80, 56, 130)
MODE_BOX = FILTER_BOX

GALLERY_BOX = (8, 190, 56, 240)

CAPTURE_BOX = (415, 130, 475, 190)

SHUTDOWN_BOX = (422, 55, 472, 105)

FILTERS = [
    "NORMAL",
    "B&W",
    "PINK",
    "SUNSET",
]


# ============================================================================
# GALLERY SCREEN
# ============================================================================

GALLERY_IMAGE_BOX = (65, 45, 415, 276)

BACK_BOX = (0, 0, 80, 30)

PREV_BOX = (8, 135, 56, 184)
NEXT_BOX = (424, 135, 472, 184)

RECENTLY_DELETED_BOX = (0, 290, 140, 320)

DELETE_BOX = (220, 290, 260, 320)

SHARE_BOX = (430, 290, 480, 320)


# ============================================================================
# RECENTLY DELETED SCREEN
# ============================================================================

RESTORE_BOX = (0, 290, 150, 320)

DELETE_FOREVER_BOX = (215, 290, 265, 320)


# ============================================================================
# SHARE SCREEN
# ============================================================================

SHARE_QR_BOX = (140, 60, 340, 260)

SHARE_BACK_BOX = (0, 0, 80, 30)

TRANSFER_PORT = 8000
TRANSFER_URL = f"http://192.168.4.1:{TRANSFER_PORT}"


# ============================================================================
# SHUTDOWN SCREEN
# ============================================================================

SHUTDOWN_CONFIRM_CANCEL_BOX = (70, 190, 210, 240)

SHUTDOWN_CONFIRM_POWER_BOX = (270, 190, 410, 240)