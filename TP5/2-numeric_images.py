from random import randint
from os import listdir

from PIL import Image
from pytest import mark


def first_exercise() -> None:
    yellow = (255, 255, 0)
    img1 = Image.new("RGB", (300, 200))
    y = 100
    for x in range(img1.size[0]):
        img1.putpixel((x, y), yellow)


def solid_rectangle(img: Image.Image, x1: int, x2: int, y1: int, y2: int, color: tuple[int, int, int]) -> None:
    for x in range(x1, x2):
        for y in range(y1, y2):
            img.putpixel((x, y), color)


@mark.xfail
def test_solid_rectangle():
    for img_path in listdir("./assets/img/"):
        original_img = Image.open(f"./assets/img/{img_path}")
        for _ in range(20):
            img = original_img.copy()
            x1 = randint(0, img.size[0] - 1)
            x2 = randint(x1, img.size[0] - 1)
            y1 = randint(0, img.size[1] - 1)
            y2 = randint(y1, img.size[1] - 1)
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            solid_rectangle(img, x1, x2, y1, y2, color)
            assert all(
                img.getpixel((x, y)) == color
                for x in range(x1, x2)
                for y in range(y1, y2)
            )


def red_filter(img: Image.Image) -> None:
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            img.putpixel((x, y), (img.getpixel((x, y))[0], 0, 0))


def test_red_filter():
    for img_path in listdir("./assets/img/"):
        img = Image.open(f"./assets/img/{img_path}")
        red_filter(img)
        assert all(
            (img.getpixel((x, y))[1] + img.getpixel((x, y))[2]) == 0
            for x in range(img.size[0])
            for y in range(img.size[1])
        )


def green_filter(img: Image.Image) -> None:
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            img.putpixel((x, y), (0, img.getpixel((x, y))[1], 0))


def test_green_filter():
    for img_path in listdir("./assets/img/"):
        img = Image.open(f"./assets/img/{img_path}")
        green_filter(img)
        assert all(
            (img.getpixel((x, y))[0] + img.getpixel((x, y))[2]) == 0
            for x in range(img.size[0])
            for y in range(img.size[1])
        )


def blue_filter(img: Image.Image) -> None:
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            img.putpixel((x, y), (0, 0, img.getpixel((x, y))[2]))


def test_blue_filter():
    for img_path in listdir("./assets/img/"):
        img = Image.open(f"./assets/img/{img_path}")
        blue_filter(img)
        assert all(
            (img.getpixel((x, y))[0] + img.getpixel((x, y))[1]) == 0
            for x in range(img.size[0])
            for y in range(img.size[1])
        )
