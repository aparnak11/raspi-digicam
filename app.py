import time

from camera import get_frame, capture_photo, stop_camera
from config import CAPTURE_BOX, GALLERY_BOX, BACK_BOX, PREV_BOX, NEXT_BOX
from display import clear_lcd
from gallery import get_photos
from touch import get_touch, in_box
from ui import draw_camera, draw_gallery


def main():
    mode = "camera"
    photo_paths = get_photos()
    gallery_index = max(0, len(photo_paths) - 1)

    try:
        while True:
            touch = get_touch()

            if mode == "camera":
                frame = get_frame()
                draw_camera(frame, "READY")

                if touch:
                    lx, ly = touch
                    print(f"touch landscape: x={lx}, y={ly}")

                    if in_box(lx, ly, CAPTURE_BOX):
                        draw_camera(frame, "SAVING...")
                        capture_photo()
                        draw_camera(frame, "SAVED!")
                        time.sleep(0.5)

                        photo_paths = get_photos()
                        gallery_index = max(0, len(photo_paths) - 1)

                    elif in_box(lx, ly, GALLERY_BOX):
                        photo_paths = get_photos()
                        gallery_index = max(0, len(photo_paths) - 1)
                        mode = "gallery"
                        draw_gallery(photo_paths, gallery_index)
                        time.sleep(0.5)

            elif mode == "gallery":
                if touch:
                    lx, ly = touch
                    print(f"gallery touch: x={lx}, y={ly}")

                    if in_box(lx, ly, BACK_BOX):
                        mode = "camera"
                        time.sleep(0.5)

                    elif in_box(lx, ly, PREV_BOX):
                        if photo_paths:
                            gallery_index = max(0, gallery_index - 1)
                            draw_gallery(photo_paths, gallery_index)
                        time.sleep(0.35)

                    elif in_box(lx, ly, NEXT_BOX):
                        if photo_paths:
                            gallery_index = min(len(photo_paths) - 1, gallery_index + 1)
                            draw_gallery(photo_paths, gallery_index)
                        time.sleep(0.35)

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        stop_camera()
        clear_lcd()


if __name__ == "__main__":
    main()