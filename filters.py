from PIL import Image, ImageEnhance


def bw_filter(image):
    return image.convert("L").convert("RGB")


def pink_filter(image):
    r, g, b = image.split()

    r = r.point(lambda p: min(255, int(p * 1.15 + 15)))
    g = g.point(lambda p: int(p * 0.92))
    b = b.point(lambda p: min(255, int(p * 1.05 + 10)))

    return Image.merge("RGB", (r, g, b))


def sunset_filter(image):
    image = ImageEnhance.Color(image).enhance(1.35)
    image = ImageEnhance.Contrast(image).enhance(1.12)

    r, g, b = image.split()

    r = r.point(lambda p: min(255, int(p * 1.35 + 25)))
    g = g.point(lambda p: int(p * 0.98 + 5))
    b = b.point(lambda p: int(p * 0.60))

    return Image.merge("RGB", (r, g, b))


FILTER_FUNCTIONS = {
    "B&W": bw_filter,
    "PINK": pink_filter,
    "SUNSET": sunset_filter,
}


def apply_filter(image, filter_name):
    filter_func = FILTER_FUNCTIONS.get(filter_name)

    if filter_func:
        return filter_func(image)

    return image