from PIL import Image


def solid_rectangle(img, x1, x2, y1, y2, color):
    for x in range(x1, x2):
        for y in range(y1, y2):
            img.putpixel((x, y), color)
    return img


def coloured_stripes(img: Image) -> Image:
    for x, color in enumerate((
            (206, 46, 234), (96, 70, 177), (18, 35, 161), (212, 205, 90),
            (84, 34, 221), (240, 153, 146), (228, 235, 244), (82, 223, 217),
            (222, 152, 14), (176, 128, 72)
    )):
        solid_rectangle(img, x * (img.size[0] // 10), (x + 1) * (img.size[0] // 10), 0, img.size[1], color)
    return img
