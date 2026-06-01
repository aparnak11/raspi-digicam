import time

from camera import get_frame, capture_photo
from config import (
    CAPTURE_BOX,
    GALLERY_BOX,
    MODE_BOX,
    BACK_BOX,
    PREV_BOX,
    NEXT_BOX,
    DELETE_BOX,
    RECENTLY_DELETED_BOX,
    RESTORE_BOX,
    DELETE_FOREVER_BOX,
    FILTERS,
)
from filters import apply_filter
from gallery import (
    get_photos,
    delete_photo,
    get_recently_deleted,
    restore_photo,
    permanently_delete_photo,
)
from touch import get_touch, in_box
from ui import draw_camera, draw_gallery
from config import DELETE_BOX
from gallery import get_photos, delete_photo
from config import SHARE_BOX, SHARE_BACK_BOX
from share_server import start_share_server
from ui import draw_camera, draw_gallery, draw_share_screen


class DigicamController:
    def __init__(self):
        self.mode = "camera"
        self.photo_paths = get_photos()
        self.gallery_index = max(0, len(self.photo_paths) - 1)
        self.filter_index = 0
        self.deleted_paths = get_recently_deleted()
        self.deleted_index = max(0, len(self.deleted_paths) - 1)
        self.previous_mode = "gallery"

    def run(self):
        while True:
            touch = get_touch()

            if self.mode == "camera":
                self.update_camera_mode(touch)

            elif self.mode == "gallery":
                self.update_gallery_mode(touch)

            elif self.mode == "deleted":
                self.update_deleted_mode(touch)

            elif self.mode == "share":
                self.update_share_mode(touch)

            time.sleep(0.05)

    def update_camera_mode(self, touch):
        frame = get_frame()
        filtered_frame = apply_filter(frame, self.current_filter())
        draw_camera(filtered_frame, "Ready", self.current_filter().title())

        if not touch:
            return

        lx, ly = touch
        print(f"touch landscape: x={lx}, y={ly}")

        if in_box(lx, ly, CAPTURE_BOX):
            self.handle_capture(filtered_frame)

        elif in_box(lx, ly, GALLERY_BOX):
            self.open_gallery()

        elif in_box(lx, ly, MODE_BOX):
            self.cycle_filter()

    def cycle_filter(self):
        self.filter_index = (self.filter_index + 1) % len(FILTERS)
        time.sleep(0.35)

    def update_gallery_mode(self, touch):
        if not touch:
            return

        lx, ly = touch
        print(f"gallery touch: x={lx}, y={ly}")
        print(f"SHARE_BOX={SHARE_BOX}, inside_share={in_box(lx, ly, SHARE_BOX)}")

        if in_box(lx, ly, BACK_BOX):
            self.mode = "camera"
            time.sleep(0.5)

        elif in_box(lx, ly, PREV_BOX):
            self.previous_photo()

        elif in_box(lx, ly, NEXT_BOX):
            self.next_photo()
        
        elif in_box(lx, ly, DELETE_BOX):
            self.delete_current_photo()
        
        elif in_box(lx, ly, RECENTLY_DELETED_BOX):
            self.open_recently_deleted()

        elif in_box(lx, ly, SHARE_BOX):
            self.open_share()

        elif in_box(lx, ly, RESTORE_BOX):
            if self.mode == "deleted":
                self.restore_current_deleted_photo()

        elif in_box(lx, ly, DELETE_FOREVER_BOX):
            if self.mode == "deleted":
                self.permanently_delete_current_photo()

        elif in_box(lx, ly, RECENTLY_DELETED_BOX):
            self.open_recently_deleted()

    def handle_capture(self, frame):
        draw_camera(frame, "Saving...", self.current_filter().title())
        time.sleep(0.2)
        capture_photo(frame)
        draw_camera(frame, "Saved!", self.current_filter().title())
        time.sleep(0.5)

        self.photo_paths = get_photos()
        self.gallery_index = max(0, len(self.photo_paths) - 1)

    def open_gallery(self):
        self.photo_paths = get_photos()
        self.gallery_index = max(0, len(self.photo_paths) - 1)

        self.mode = "gallery"
        draw_gallery(self.photo_paths, self.gallery_index)
        time.sleep(0.5)

    def previous_photo(self):
        if self.photo_paths:
            self.gallery_index = max(0, self.gallery_index - 1)
            draw_gallery(self.photo_paths, self.gallery_index)

        time.sleep(0.35)

    def next_photo(self):
        if self.photo_paths:
            self.gallery_index = min(len(self.photo_paths) - 1, self.gallery_index + 1)
            draw_gallery(self.photo_paths, self.gallery_index)

        time.sleep(0.35)

    def delete_current_photo(self):
        if not self.photo_paths:
            return

        photo_to_delete = self.photo_paths[self.gallery_index]
        delete_photo(photo_to_delete)

        self.photo_paths = get_photos()

        if not self.photo_paths:
            self.gallery_index = 0
        else:
            self.gallery_index = min(self.gallery_index, len(self.photo_paths) - 1)

        draw_gallery(self.photo_paths, self.gallery_index)
        time.sleep(0.5)

    def current_filter(self):
        return FILTERS[self.filter_index]

    def open_recently_deleted(self):
        self.deleted_paths = get_recently_deleted()
        self.deleted_index = max(0, len(self.deleted_paths) - 1)
        self.mode = "deleted"
        draw_gallery(self.deleted_paths, self.deleted_index, deleted_mode=True)
        time.sleep(0.5)


    def update_deleted_mode(self, touch):
        if not touch:
            return

        lx, ly = touch
        print(f"deleted touch: x={lx}, y={ly}")

        print(f"RESTORE={in_box(lx, ly, RESTORE_BOX)}")
        print(f"DELETE_FOREVER={in_box(lx, ly, DELETE_FOREVER_BOX)}")
        print(f"SHARE={in_box(lx, ly, SHARE_BOX)}")

        if in_box(lx, ly, BACK_BOX):
            self.mode = "gallery"
            self.photo_paths = get_photos()
            self.gallery_index = max(0, len(self.photo_paths) - 1)
            draw_gallery(self.photo_paths, self.gallery_index)
            time.sleep(0.5)

        elif in_box(lx, ly, SHARE_BOX):
            self.open_share()

        elif in_box(lx, ly, RESTORE_BOX):
            self.restore_current_deleted_photo()

        elif in_box(lx, ly, DELETE_FOREVER_BOX):
            self.permanently_delete_current_photo()

        elif in_box(lx, ly, PREV_BOX):
            if self.deleted_paths:
                self.deleted_index = max(0, self.deleted_index - 1)
                draw_gallery(self.deleted_paths, self.deleted_index, deleted_mode=True)
            time.sleep(0.35)

        elif in_box(lx, ly, NEXT_BOX):
            if self.deleted_paths:
                self.deleted_index = min(len(self.deleted_paths) - 1, self.deleted_index + 1)
                draw_gallery(self.deleted_paths, self.deleted_index, deleted_mode=True)
            time.sleep(0.35)

    def restore_current_deleted_photo(self):
        if not self.deleted_paths:
            return

        photo_to_restore = self.deleted_paths[self.deleted_index]
        restore_photo(photo_to_restore)

        self.deleted_paths = get_recently_deleted()

        if not self.deleted_paths:
            self.deleted_index = 0
        else:
            self.deleted_index = min(self.deleted_index, len(self.deleted_paths) - 1)

        draw_gallery(self.deleted_paths, self.deleted_index, deleted_mode=True)
        time.sleep(0.5)


    def permanently_delete_current_photo(self):
        if not self.deleted_paths:
            return

        photo_to_delete = self.deleted_paths[self.deleted_index]
        permanently_delete_photo(photo_to_delete)

        self.deleted_paths = get_recently_deleted()

        if not self.deleted_paths:
            self.deleted_index = 0
        else:
            self.deleted_index = min(self.deleted_index, len(self.deleted_paths) - 1)

        draw_gallery(self.deleted_paths, self.deleted_index, deleted_mode=True)
        time.sleep(0.5)
    
    def open_share(self):
        print("Opening share screen...")

        self.previous_mode = self.mode

        self.mode = "share"
        draw_share_screen()
        print("Share screen drawn")

        start_share_server()
        print("Share server started")

        time.sleep(0.5)


    def update_share_mode(self, touch):
        if not touch:
            return

        lx, ly = touch
        print(f"share touch: x={lx}, y={ly}")

        if in_box(lx, ly, SHARE_BACK_BOX):
            if self.previous_mode == "deleted":
                self.mode = "deleted"
                self.deleted_paths = get_recently_deleted()
                self.deleted_index = max(0, len(self.deleted_paths) - 1)
                draw_gallery(self.deleted_paths, self.deleted_index, deleted_mode=True)
            else:
                self.mode = "gallery"
                self.photo_paths = get_photos()
                self.gallery_index = max(0, len(self.photo_paths) - 1)
                draw_gallery(self.photo_paths, self.gallery_index)

            time.sleep(0.5)