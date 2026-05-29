from camera import stop_camera
from controller import DigicamController
from display import clear_lcd


def main():
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