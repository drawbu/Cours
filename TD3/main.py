from PIL import Image


def solid_rectangle(img, x1, x2, y1, y2, color):
    for x in range(x1, x2):
        for y in range(y1, y2):
            pixel = img.getpixel((x, y))
            print(f"{x=}, {y=}, {pixel}")
            img.putpixel((x, y), color)
    return img


if __name__ == "__main__":
    YELLOW = (255, 0, 0)
    img = Image.new("RGB", (300, 200))
    solid_rectangle(img, 0, 50, 0, 100, YELLOW)
    img.show()
