import time

from camera import get_frame, capture_photo
from config import (
    CAPTURE_BOX,
    GALLERY_BOX,
    MODE_BOX,
    BACK_BOX,
    PREV_BOX,
    NEXT_BOX,
    FILTERS,
)
from filters import apply_filter
from gallery import get_photos
from touch import get_touch, in_box
from ui import draw_camera, draw_gallery
from config import DELETE_BOX
from gallery import get_photos, delete_photo


class DigicamController:
    def __init__(self):
        self.mode = "camera"
        self.photo_paths = get_photos()
        self.gallery_index = max(0, len(self.photo_paths) - 1)
        self.filter_index = 0

    def run(self):
        while True:
            touch = get_touch()

            if self.mode == "camera":
                self.update_camera_mode(touch)

            elif self.mode == "gallery":
                self.update_gallery_mode(touch)

            time.sleep(0.05)

    def update_camera_mode(self, touch):
        frame = get_frame()
        filtered_frame = apply_filter(frame, self.current_filter())
        draw_camera(filtered_frame, "READY", self.current_filter())

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

        if in_box(lx, ly, BACK_BOX):
            self.mode = "camera"
            time.sleep(0.5)

        elif in_box(lx, ly, PREV_BOX):
            self.previous_photo()

        elif in_box(lx, ly, NEXT_BOX):
            self.next_photo()
        
        elif in_box(lx, ly, DELETE_BOX):
            self.delete_current_photo()

    def handle_capture(self, frame):
        draw_camera(frame, "SAVING...", self.current_filter())
        capture_photo(frame)
        draw_camera(frame, "SAVED!", self.current_filter())
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