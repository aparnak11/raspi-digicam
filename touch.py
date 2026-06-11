from vendor.waveshare import ft6336u


TOUCH_WIDTH = 320
TOUCH_HEIGHT = 480


def create_touchscreen():
    return ft6336u.ft6336u()


tp = create_touchscreen()


def touch_to_landscape(x, y):
    lx = TOUCH_HEIGHT - y
    ly = TOUCH_WIDTH - x
    return lx, ly


def in_box(lx, ly, box):
    x1, y1, x2, y2 = box
    return x1 <= lx <= x2 and y1 <= ly <= y2


def get_touch():
    try:
        tp.read_touch_data()
        point_count, coords = tp.get_touch_xy()

        if point_count <= 0 or not coords:
            return None

        x = coords[0]["x"]
        y = coords[0]["y"]

        if not (0 <= x <= TOUCH_WIDTH and 0 <= y <= TOUCH_HEIGHT):
            return None

        return touch_to_landscape(x, y)

    except OSError:
        return None