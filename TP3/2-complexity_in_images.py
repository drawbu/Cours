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
        solid_rectangle(
            img,
            x * (img.size[0] // 10),
            (x + 1) * (img.size[0] // 10),
            0,
            img.size[1],
            color
        )
    return img


def minimum_colors(img: Image) -> list[int, int, int]:
    minimum = [255, 255, 255]
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            for i in range(len(minimum)):
                if minimum[i] > img.getpixel((x, y))[i]:
                    minimum[i] = img.getpixel((x, y))[i]
    return minimum


def maximum_colors(img: Image) -> list[int, int, int]:
    maximum = [0, 0, 0]
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            for i in range(len(maximum)):
                if maximum[i] < img.getpixel((x, y))[i]:
                    maximum[i] = img.getpixel((x, y))[i]
    return maximum


def color_vector(color, minimum, maximum) -> tuple[int, int, int]:
    return (
        (255 * (color[0] - minimum[0])) // (maximum[0] - minimum[0]),
        (255 * (color[1] - minimum[1])) // (maximum[1] - minimum[1]),
        (255 * (color[2] - minimum[2])) // (maximum[2] - minimum[2]),
    )


def renew_color_levels(img: Image):
    maximum = maximum_colors(img)
    minimum = minimum_colors(img)
    for x in range(img.size[0]):
        for y in range(img.size[0]):
            color = img.getpixel((x, y))
            img.putpixel(
                (x, y),
                color_vector(color, minimum, maximum)
            )
    return img


# Tests
def tests() -> None:
    img1 = Image.new("RGB", (300, 300))
    img2 = coloured_stripes(Image.new("RGB", (300, 300)))
    img3 = Image.open("./TP3/img/lion.jpeg")
    img4 = Image.open("./TP3/img/hell.png")

    # minimum_colors
    assert minimum_colors(img1) == [0, 0, 0]
    assert minimum_colors(img2) == [18, 34, 14]
    assert minimum_colors(img3) == [0, 0, 0]
    assert minimum_colors(img4) == [0, 88, 9]

    # maximum_colors
    assert maximum_colors(img1) == [0, 0, 0]
    assert maximum_colors(img2) == [240, 235, 244]
    assert maximum_colors(img3) == [255, 244, 228]
    assert maximum_colors(img4) == [0, 89, 13]


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300))
    img = coloured_stripes(img)
    img = renew_color_levels(img)
    img.show()
