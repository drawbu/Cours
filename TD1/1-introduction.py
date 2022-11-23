from array import array
from random import randint


# Insert
def insert(t: array, n: int, elt: any, k: int) -> None:
    t.append(0)
    for i in range(n, k - 1, -1):
        t[i] = elt if i == k else t[i - 1]


def test_insert():
    for i in range(1, 21):
        arr = array("b", [randint(0, 10) for _ in range(i)])
        elt = randint(0, 10)
        k = randint(0, len(arr) - 1)
        insert(arr, len(arr), elt, k)
        assert arr[k] == elt


# Delete
def delete(t: array, n: int, k: int) -> int:
    if k + 1 == n:
        return n - 1
    for i in range(k, n - 1):
        t[i] = t[i + 1]
    return n - 1


def test_delete():
    for i in range(2, 21):
        arr = array("b", [randint(0, 10) for _ in range(i)])
        k = randint(0, len(arr) - 1)
        original_value = arr[k]
        original_value_next = arr[k + 1] if k + 1 != len(arr) else arr[0]

        result = delete(arr, len(arr), k)
        assert int(result)
        assert result == len(arr) - 1
        if k + 1 == len(arr):
            return
        if original_value != original_value_next:
            assert arr[k] != original_value

        assert arr[-1] == arr[-2]


# Amplitude
def amplitude(t: array, n: int) -> int:
    v_max = t[0]
    v_min = t[0]
    for i in range(n):
        if v_max < t[i]:
            v_max = t[i]
            continue
        if v_min > t[i]:
            v_min = t[i]
    return v_max - v_min


def test_amplitude():
    for i in range(1, 21):
        arr = array("b", [randint(0, 10) for _ in range(i)])
        n = randint(1, len(arr))
        assert amplitude(arr, n) == abs(max(arr[:n]) - min(arr[:n]))


# Max v2
def max2(t: array, n: int):
    print(t)
    max_1 = min(t)
    max_2 = max_1
    for i in range(n):
        print(t[i])
        if t[i] > max_1:
            max_2 = max_1
            max_1 = t[i]
            continue
        if t[i] > max_2:
            max_2 = t[i]
    return max_2


def test_max2():
    arr = array("b", [5, 3, 4, 6, 1, 10, 2, 10, 4])
    assert max2(arr, 5) == 5
    assert max2(arr, 9) == 10


# Delete first instance
def delete_first_instance(t: array, n: int, elt: any):
    for i in range(n):
        if t[i] == elt:
            delete(t, n, i)
            return


def test_delete_first_instance():
    for i in range(1, 21):
        arr = array("b", [randint(0, 10) for _ in range(i)])
        original_arr = array("b", arr)
        elt = randint(0, 10)
        if elt not in arr:
            delete_first_instance(arr, len(arr), elt)
            assert arr == original_arr
            continue

        index = arr.index(elt)
        if index + 1 == len(arr):
            continue

        elt_next = arr[index + 1]
        delete_first_instance(arr, len(arr), elt)

        if elt != elt_next:
            assert arr[index] != elt


# Un_duplicated
def un_duplicated(t: array, n: int) -> bool:
    for i in range(n):
        for j in range(i+1, n):
            if t[i] == t[j]:
                return False
    return True


def test_un_duplicated():
    for i in range(1, 21):
        arr = array("b", [randint(0, 10) for _ in range(i)])
        should_result = sorted(arr) == sorted(set(arr))
        assert un_duplicated(arr, len(arr)) == should_result


# Delete instances
def delete_instances(t: array, n: int, elt: int):
    instances = 0
    for i in range(n):
        if t[i] == elt:
            instances += 1
            continue
        t[i - instances] = t[i]
    return n - instances


def test_delete_instances():
    for i in range(8, 21):
        arr = array("b", [randint(0, 10) for _ in range(i)])
        elt = randint(0, 10)
        should_result = len(arr) - arr.count(elt)
        result = delete_instances(arr, len(arr), elt)
        assert isinstance(result, int)
        assert result == should_result
        assert arr[:result].count(elt) == 0
