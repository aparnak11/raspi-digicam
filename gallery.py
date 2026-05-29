from PIL import Image

from config import PHOTOS_DIR


def get_photos():
    return sorted(PHOTOS_DIR.glob("*.jpg"), key=lambda p: p.stat().st_mtime)


def load_gallery_image(photo_paths, gallery_index):
    if not photo_paths:
        return None, None

    photo_path = photo_paths[gallery_index]
    photo = Image.open(photo_path).convert("RGB")
    photo.thumbnail((300, 220))

    return photo, photo_path
