import time

from camera import stop_camera
from controller import DigicamController
from display import clear_lcd
from ui import draw_shutdown_splash, draw_splash


STARTUP_DELAY_SECONDS = 1.5
SHUTDOWN_SAVE_DELAY_SECONDS = 0.75
SHUTDOWN_GOODBYE_DELAY_SECONDS = 1.0


def main():
    draw_splash("Loading...")
    time.sleep(STARTUP_DELAY_SECONDS)

    controller = DigicamController()

    try:
        controller.run()

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        shutdown_cleanly()


def shutdown_cleanly():
    draw_shutdown_splash("Saving...")
    time.sleep(SHUTDOWN_SAVE_DELAY_SECONDS)

    stop_camera()

    draw_shutdown_splash("Goodbye!")
    time.sleep(SHUTDOWN_GOODBYE_DELAY_SECONDS)

    clear_lcd()


if __name__ == "__main__":
    main()