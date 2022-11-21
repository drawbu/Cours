import timeit
from typing import Any
from array import array


def binary_search(x: Any, tab: array, n: int) -> int:
    left = 0
    right = n - 1
    while left <= right:
        m = (left + right) // 2
        if tab[m] < x:
            left = m + 1
            continue
        if tab[m] > x:
            right = m - 1
            continue
        return m
    return -1


def modified_binary_search(x: Any, tab: array, n: int) -> int:
    if x > tab[n - 1]:
        return -1

    left = 0
    right = n - 1

    while left <= right:
        if x > tab[right]:
            return -1
        if x < tab[left]:
            return -1

        if x == tab[right]:
            return right
        if x == tab[left]:
            return left

        m = (left + right) // 2
        if tab[m] < x:
            left = m + 1
            continue
        if tab[m] > x:
            right = m - 1
            continue
        return m
    return -1


def tests():
    tab1 = array("l", list(range(10)))
    tab2 = array("l", [1, 4, 21, 53, 64, 98, 102, 171, 188, 205])

    # binary search
    assert binary_search(2, tab1, len(tab1)) == 2
    assert binary_search(11, tab1, len(tab1)) == -1
    assert binary_search(64, tab2, len(tab2)) == 4
    assert binary_search(206, tab2, len(tab2)) == -1

    # modified binary search
    assert modified_binary_search(2, tab1, len(tab1)) == 2
    assert modified_binary_search(11, tab1, len(tab1)) == -1
    assert modified_binary_search(64, tab2, len(tab2)) == 4
    assert modified_binary_search(206, tab2, len(tab2)) == -1


if __name__ == "__main__":
    tests()

    arr = array("l", [1, 4, 21, 53, 64, 98, 102, 171, 188, 205])
    n_tests = 10_000_000
    elem = 205


    def timer(func) -> float:
        return timeit.timeit(lambda: func(elem, arr, len(arr)), number=n_tests)


    print(f"With {n_tests:,} run for each:")
    print(f"binary_search:          {timer(binary_search):.2f}s")
    print(f"modified_binary_search: {timer(modified_binary_search):.2f}s")
