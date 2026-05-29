from PIL import Image, ImageDraw
import st7796

lcd = st7796.st7796()
lcd.lcd_init()
lcd.clear()

# Colors
bg = "#fffafc"
white = "#ffffff"
black = "#111111"
pink = "#d96c93"
light_pink = "#f4c2d7"
dark_pink = "#b84f74"
gray = "#888888"

W, H = lcd.width, lcd.height

# LANDSCAPE CANVAS
LW, LH = 480, 320
image = Image.new("RGB", (LW, LH), bg)
draw = ImageDraw.Draw(image)

# Top bar
draw.rectangle((0, 0, LW, 36), fill=light_pink)
draw.text((14, 10), "APARNA'S DIGICAM", fill=black)
draw.text((LW - 62, 10), "64GB", fill=black)

# Center viewfinder
vf_x1, vf_y1 = 92, 52
vf_x2, vf_y2 = 388, 255
draw.rectangle((vf_x1, vf_y1, vf_x2, vf_y2), outline=pink, width=3)

# Focus brackets
draw.line((120, 78, 155, 78), fill=dark_pink, width=3)
draw.line((120, 78, 120, 113), fill=dark_pink, width=3)

draw.line((360, 78, 325, 78), fill=dark_pink, width=3)
draw.line((360, 78, 360, 113), fill=dark_pink, width=3)

draw.line((120, 230, 155, 230), fill=dark_pink, width=3)
draw.line((120, 230, 120, 195), fill=dark_pink, width=3)

draw.line((360, 230, 325, 230), fill=dark_pink, width=3)
draw.line((360, 230, 360, 195), fill=dark_pink, width=3)

# Center focus box
draw.rectangle((220, 135, 260, 172), outline=gray, width=2)

# Left controls
draw.rounded_rectangle((12, 70, 76, 125), radius=12, fill=light_pink, outline=pink, width=2)
draw.text((22, 90), "MODE", fill=black)

draw.rounded_rectangle((12, 155, 76, 210), radius=12, fill=light_pink, outline=pink, width=2)
draw.text((18, 175), "GALLERY", fill=black)

# Right capture button
draw.ellipse((405, 120, 465, 180), outline=dark_pink, width=5)
draw.ellipse((420, 135, 450, 165), fill=pink)

draw.text((410, 190), "CAPTURE", fill=black)

# Bottom status
draw.rectangle((0, LH - 32, LW, LH), fill=light_pink)
draw.text((18, LH - 22), "READY", fill=black)
draw.text((LW - 70, LH - 22), "PHOTO", fill=black)

# Convert landscape canvas to your physical display orientation
image = image.rotate(90, expand=True)
image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

lcd.show_image(image)

input("Press Enter to exit...")
