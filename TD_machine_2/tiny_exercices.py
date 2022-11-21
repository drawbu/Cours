from random import randint
from array import array
from string import ascii_lowercase


def sum_int(n: int):
    if n == 0:
        return 0
    return n + sum_int(n - 1)


def sum_array(t: array, n: int):
    if n == 1:
        return t[n - 1]
    return t[n - 1] + sum_array(t, n - 1)


def complete_bin(t: array, n: int):
    if n == 0:
        return t
    if t[n - 1] == 1:
        t[n - 1] = 0
    else:
        t[n - 1] = 1
    return complete_bin(t, n - 1)


def reverse(t, n, i=0):
    if n == 1:
        return array("u", t[0])
    return array("u", t[n - 1]) + reverse(t, n - 1, i)


def sum_array_rec(t: array, n: int, i: int = 0):
    if i == n - 1:
        return t[i]
    return t[i] + sum_array_rec(t, n, i + 1)


def is_sorted(t: array, n: int):
    if n == 1:
        return True
    if t[n - 1] >= t[n - 2]:
        return is_sorted(t, n - 1)
    return False


def pair(n: int):
    if n == 1:
        return "impair"
    return impair(n - 1)


def impair(n: int):
    if n == 1:
        return "pair"
    return pair(n - 1)


def maximum(t: array, n: int):
    if n == 1:
        return t[n - 1]
    maxi = maximum(t, n - 1)
    if maxi < t[n - 1]:
        return t[n - 1]
    return maxi


def prime_number(n: int, i: int = 2):
    if i == n or n == 1:
        return True
    if n % i == 0:
        print(f"{n=}; {i=}")
        return False
    return prime_number(n, i + 1)


def tests():
    # sum_int
    for i in range(1, 21):
        assert sum_int(i) == sum(range(i + 1))

    # sum_array
    for i in range(1, 21):
        tab = array("H", [randint(0, 10) for _ in range(i)])
        assert sum_array(tab, len(tab)) == sum(tab)

    # one_complement
    assert complete_bin(array("i", [1, 1, 1, 0]), 4) == array("i", [0, 0, 0, 1])
    assert complete_bin(array("i", [0, 1, 1, 0]), 4) == array("i", [1, 0, 0, 1])
    assert complete_bin(array("i", [0, 0, 0, 0]), 4) == array("i", [1, 1, 1, 1])
    assert complete_bin(array("i", [1, 1, 1, 1]), 4) == array("i", [0, 0, 0, 0])

    # reverse
    for i in range(1, 21):
        tab = array("u", [ascii_lowercase[randint(0, 25)] for _ in range(i)])
        assert reverse(tab, len(tab)) == array("u", reversed(tab))

    # sum_array_rec
    for i in range(1, 21):
        tab = array("H", [randint(0, 10) for _ in range(i)])
        assert sum_array_rec(tab, len(tab)) == sum(tab)

    # is_sorted
    for i in range(1, 21):
        tab = array("H", [randint(0, 10) for _ in range(i)])
        sorted_tab = array("H", sorted(tab))
        assert is_sorted(sorted_tab, len(tab)) is True
        assert is_sorted(tab, len(tab)) == (sorted_tab == tab)

    for i in range(1, 21):
        assert pair(i) == ("impair" if i % 2 else "pair")

    for i in range(1, 21):
        tab = array("H", [randint(0, 100) for _ in range(i)])
        assert maximum(tab, len(tab)) == max(tab)

    for n, is_prime in {
        1: True,
        3: True,
        6: False,
        8: False,
        13: True,
        15: False,
    }.items():
        assert prime_number(n) == is_prime


if __name__ == "__main__":
    tests()
