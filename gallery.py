import shutil
from PIL import Image

from config import PHOTOS_DIR, RECENTLY_DELETED_DIR


def get_jpgs(directory):
    return sorted(directory.glob("*.jpg"), key=lambda p: p.stat().st_mtime)


def get_available_path(directory, filename):
    path = directory / filename

    counter = 1
    while path.exists():
        path = directory / f"{path.stem}_{counter}{path.suffix}"
        counter += 1

    return path


def move_photo(photo_path, destination_dir):
    destination_path = get_available_path(destination_dir, photo_path.name)
    shutil.move(str(photo_path), str(destination_path))
    return destination_path


def get_photos():
    return get_jpgs(PHOTOS_DIR)


def get_recently_deleted():
    return get_jpgs(RECENTLY_DELETED_DIR)


def load_gallery_image(photo_paths, gallery_index):
    if not photo_paths:
        return None, None

    photo_path = photo_paths[gallery_index]
    photo = Image.open(photo_path).convert("RGB")
    photo.thumbnail((300, 220))

    return photo, photo_path


def delete_photo(photo_path):
    return move_photo(photo_path, RECENTLY_DELETED_DIR)


def restore_photo(photo_path):
    return move_photo(photo_path, PHOTOS_DIR)


def permanently_delete_photo(photo_path):
    photo_path.unlink()