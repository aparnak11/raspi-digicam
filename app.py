import time

from ui import draw_splash, draw_shutdown_splash
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
        draw_shutdown_splash("Saving...")
        time.sleep(0.75)

        stop_camera()

        draw_shutdown_splash("Goodbye!")
        time.sleep(1.0)

        clear_lcd()


if __name__ == "__main__":
    main()