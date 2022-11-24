from array import array
from random import randint, choice
from typing import Optional, Any


# Monotonicity
def monotonicity(arr: array, n: int) -> tuple[int, Optional[int]]:
    if n == 0:
        return 0, None

    mono = 1
    index = None
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            mono = 1
            index = None
            continue

        mono += 1
        if index is None:
            index = i
    return mono, index


def test_monotonicity():
    arr = array("b", [2, 7, 3, 0, 3, 8, 10, 7])
    assert monotonicity(arr, len(arr)) == (1, None)

    arr = array("b", [2, 7, 3, 2, 3, 8, 10, 11])
    assert monotonicity(arr, len(arr)) == (5, 3)

    arr = array("b", [1, 2, 3, 4, 5, 6, 7, 8])
    assert monotonicity(arr, len(arr)) == (8, 0)

    arr = array("b", [1, 2, 3, 4, 5, 6, 7, 7])
    assert monotonicity(arr, len(arr)) == (8, 0)

    arr = array("b", [1, 1, 1, 1, 1, 1, 1, 1])
    assert monotonicity(arr, len(arr)) == (8, 0)

    arr = array("b", [1, 1, 1, 1, 1, 1, 1, 0])
    assert monotonicity(arr, len(arr)) == (1, None)


# Search
def search(arr: array, n: int, elt: Any) -> int:
    for i in range(n - 1, -1, -1):
        if arr[i] == elt:
            return i
    return -1


def test_search():
    for i in range(1, 21):
        arr = array("b", [randint(0, 10) for _ in range(i)])
        elt = randint(0, 10)
        result = search(arr, len(arr), elt)
        assert isinstance(result, int)
        if elt not in arr:
            assert result == -1
            continue
        assert result == len(arr) - list(reversed(arr)).index(elt) - 1


# Swap
def swap(arr: array, i: int, j: int) -> None:
    elt = arr[i]
    arr[i] = arr[j]
    arr[j] = elt


def test_swap():
    for i in range(1, 21):
        arr = array("b", [randint(0, 10) for _ in range(i)])
        param_i = randint(0, i - 1)
        param_j = randint(0, i - 1)

        original_arr = array("b", arr)
        swap(arr, param_i, param_j)
        assert arr[param_i] == original_arr[param_j]
        assert arr[param_j] == original_arr[param_i]


# Insert order
def insert_order(arr: array, n: int, elt: int) -> int:
    for i in range(n):
        if arr[i] <= elt:
            continue
        for j in range(n, i, -1):
            arr[j] = arr[j - 1]
        arr[i] = elt
        return n + 1
    arr[n] = elt
    return n + 1


def test_insert_order():
    for i in range(2, 21):
        arr = array("b", sorted(randint(0, 10) for _ in range(i)))
        elt = randint(0, 10)
        rand = randint(1, i - 1)
        n = len(arr) - rand
        count_elt = arr[:n].count(elt)
        result = insert_order(arr, n, elt)
        assert isinstance(result, int)
        assert result == n + 1
        assert arr[:n + 1] == array("b", sorted(arr[:n + 1]))
        assert count_elt + 1 == arr[:n + 1].count(elt)


def separate(arr: array, n: int) -> None:
    i = 0
    j = n - 1
    while i < j:
        if arr[i] == 1:
            swap(arr, i, j)
            j -= 1
            continue
        i += 1


def test_separate():
    for i in range(1, 21):
        arr = array("b", [randint(0, 1) for _ in range(i)])
        separate(arr, len(arr))
        if 1 not in arr:
            continue
        index = arr.index(1)
        assert all(e == 0 for e in arr[:index])
        assert all(e == 1 for e in arr[index:])


def is_section(arr: array, n_arr: int, s, n_s) -> bool:
    for i in range(n_arr - n_s):
        found = True
        for j in range(0, n_s):
            if arr[i + j] != s[j]:
                found = False
                break
        if found:
            return True
    return False


def test_is_section():
    arr = array("b", [5, 1, 2, 3, 1, 2, 1])
    section = [1, 2]
    result = is_section(arr, len(arr), section, len(section))
    assert isinstance(result, bool)
    assert result == True

    arr = array("b", [1, 2, 3, 4, 1])
    section = [1, 3]
    result = is_section(arr, len(arr), section, len(section))
    assert isinstance(result, bool)
    assert result == False


def highest_score(students: list, scores: array, n: int) -> list[str]:
    result = []
    for i in range(n):
        if scores[i] == 20:
            result.append(students[i])
    return result


def test_highest_score():
    for i in range(1, 21):
        students = [choice((
            "bob", "clement", "carole", "jodie", "maxime", "roger", "xavier",
            "edouard", "phillipe", "sylvain", "alexis", "jules", "jean",
            "claude", "didier", "timothy", "gregory", "mathis"
        )) for _ in range(i)]
        scores = array("b", [randint(0, 20) for _ in range(i)])
        result = highest_score(students, scores, i)
        assert isinstance(result, list)
        assert all(isinstance(e, str) for e in result)

        should_result = [students[j] for j in range(i) if scores[j] == 20]
        assert result == should_result
