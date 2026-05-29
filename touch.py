from vendor.waveshare import ft6336u

tp = ft6336u.ft6336u()


def touch_to_landscape(x, y):
    lx = 480 - y
    ly = 320 - x
    return lx, ly


def in_box(lx, ly, box):
    x1, y1, x2, y2 = box
    return x1 <= lx <= x2 and y1 <= ly <= y2


def get_touch():
    tp.read_touch_data()
    point_count, coords = tp.get_touch_xy()

    if point_count > 0:
        raw_x = coords[0]["x"]
        raw_y = coords[0]["y"]
        return touch_to_landscape(raw_x, raw_y)

    return None
