from PIL import Image, ImageDraw
import st7796
import ft6336u
import time

lcd = st7796.st7796()
lcd.lcd_init()
lcd.clear()

tp = ft6336u.ft6336u()

# Colors
bg = "#fffafc"
black = "#111111"
pink = "#d96c93"
light_pink = "#f4c2d7"
dark_pink = "#b84f74"
gray = "#888888"

LW, LH = 480, 320

def show_on_lcd(image):
    image = image.rotate(90, expand=True)
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    lcd.show_image(image)

def draw_ui(message="Touch screen"):
    image = Image.new("RGB", (LW, LH), bg)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, LW, 36), fill=light_pink)
    draw.text((14, 10), "APARNA'S DIGICAM", fill=black)

    draw.rectangle((92, 52, 388, 255), outline=pink, width=3)
    draw.text((190, 145), message, fill=black)

    draw.rounded_rectangle((12, 155, 76, 210), radius=12, fill=light_pink, outline=pink, width=2)
    draw.text((18, 175), "GALL", fill=black)

    draw.ellipse((405, 120, 465, 180), outline=dark_pink, width=5)
    draw.ellipse((420, 135, 450, 165), fill=pink)
    draw.text((410, 190), "CAPTURE", fill=black)

    draw.rectangle((0, LH - 32, LW, LH), fill=light_pink)
    draw.text((18, LH - 22), "TOUCH TEST", fill=black)

    show_on_lcd(image)

draw_ui()

try:
    while True:
        tp.read_touch_data()
        point_count, coords = tp.get_touch_xy()

        if point_count > 0:
            x = coords[0]["x"]
            y = coords[0]["y"]

            print(f"raw touch: x={x}, y={y}")

            draw_ui(f"x={x}, y={y}")

            time.sleep(0.3)

        time.sleep(0.05)

except KeyboardInterrupt:
    lcd.clear()
