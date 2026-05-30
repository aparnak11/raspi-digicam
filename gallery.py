from PIL import Image

from config import PHOTOS_DIR, RECENTLY_DELETED_DIR
import shutil


def get_photos():
    return sorted(PHOTOS_DIR.glob("*.jpg"), key=lambda p: p.stat().st_mtime)


def load_gallery_image(photo_paths, gallery_index):
    if not photo_paths:
        return None, None

    photo_path = photo_paths[gallery_index]
    photo = Image.open(photo_path).convert("RGB")
    photo.thumbnail((300, 220))

    return photo, photo_path

def delete_photo(photo_path):
    deleted_path = RECENTLY_DELETED_DIR / photo_path.name

    counter = 1
    while deleted_path.exists():
        deleted_path = RECENTLY_DELETED_DIR / f"{photo_path.stem}_{counter}{photo_path.suffix}"
        counter += 1

    shutil.move(str(photo_path), str(deleted_path))
    return deleted_path
