from PIL import Image
from vendor.waveshare import st7796

lcd = st7796.st7796()
lcd.lcd_init()
lcd.clear()

def show_on_lcd(image):
    image = image.rotate(90, expand=True)
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    lcd.show_image(image)

def clear_lcd():
    lcd.clear()