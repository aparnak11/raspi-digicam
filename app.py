import time

from ui import draw_splash
from camera import stop_camera
from controller import DigicamController
from display import clear_lcd


def main():
    draw_splash("Loading...")
    time.sleep(1.5)

    controller = DigicamController()

    try:
        controller.run()

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        stop_camera()
        clear_lcd()


if __name__ == "__main__":
    main()