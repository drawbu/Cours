from array import array


def egyptian_fraction2(a: int, b: int, t: array, i: int = 0) -> int:
    if a == 1:
        t[i] = b
        return i
    i = egyptian_fraction2(1, b, t, i)
    i = egyptian_fraction2(a - 1, b + 1, t, i + 1)
    i = egyptian_fraction2(a - 1, b * (b + 1), t, i + 1)
    return i


def tests():
    tab = array("l", [0] * 10)
    egyptian_fraction2(3, 5, tab)
    assert tab == array("l", [5, 6, 7, 42, 30, 31, 930, 0, 0, 0])


if __name__ == "__main__":
    tests()
