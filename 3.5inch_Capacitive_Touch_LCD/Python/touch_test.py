import ft6336u
import time

tp = ft6336u.ft6336u()

while True:
    try:
        tp.read_touch_data()
        point_count, coords = tp.get_touch_xy()

        if point_count > 0:
            x = coords[0]["x"]
            y = coords[0]["y"]
            print(f"x={x}, y={y}")

        time.sleep(0.05)

    except KeyboardInterrupt:
        break
