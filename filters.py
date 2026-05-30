from PIL import Image, ImageEnhance


def apply_filter(image, filter_name):
    if filter_name == "B&W":
        return image.convert("L").convert("RGB")

    if filter_name == "PINK":
        r, g, b = image.split()
        r = r.point(lambda p: min(255, int(p * 1.15 + 15)))
        g = g.point(lambda p: int(p * 0.92))
        b = b.point(lambda p: min(255, int(p * 1.05 + 10)))
        return Image.merge("RGB", (r, g, b))

    if filter_name == "VINTAGE":
        image = ImageEnhance.Color(image).enhance(0.75)
        image = ImageEnhance.Contrast(image).enhance(1.15)
        image = ImageEnhance.Brightness(image).enhance(1.05)

        r, g, b = image.split()
        r = r.point(lambda p: min(255, int(p * 1.08 + 8)))
        g = g.point(lambda p: min(255, int(p * 1.02 + 4)))
        b = b.point(lambda p: int(p * 0.88))
        return Image.merge("RGB", (r, g, b))

    return image
