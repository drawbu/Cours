import random
from array import array


# Roll dices
def roll_dices(n: int) -> array:
    result = array("H", [0] * n)
    for i in range(n):
        result[i] = random.randint(1, 6)
    return result


def test_roll_dices():
    for i in range(1, 21):
        dices = roll_dices(i)
        assert len(dices) == i
        for dice in dices:
            assert dice in range(1, 7)


# Sum values
def sum_values(t: array, n: int) -> int:
    total = 0
    for i in range(n):
        total += t[i]
    return total


def test_sum_values():
    for i in range(1, 21):
        dices = roll_dices(i)
        assert sum_values(dices, len(dices)) == sum(dices)


# Number of dice with same value
def number_of_dice_with_same_value(t: array, n: int, value: int) -> int:
    result = 0
    for i in range(n):
        if t[i] == value:
            result += 1
    return result


def test_number_of_dice_with_same_value():
    for i in range(1, 21):
        dices = roll_dices(i)
        value = random.randint(1, 7)
        assert (
                number_of_dice_with_same_value(dices, len(dices), value)
                ==
                dices.count(value)
        )


# Histogram
def histogram(t: array, n: int, m: int = None) -> array:
    result = array("H", [n, 0, 0, 0, 0, 0, 0])

    if m is None:
        for i in range(n):
            result[t[i]] += 1
        return result

    for _ in range(m):
        t = roll_dices(n)
        for i in range(n):
            result[t[i]] += 1
    return result


def test_histogram():
    for i in range(1, 21):
        dices = roll_dices(i)
        histo = histogram(dices, len(dices))
        assert histo == array(
            "H", [len(dices)] + [dices.count(j) for j in range(1, 7)]
        )
        assert sum(histo) == i * 2


def test_histogram_multiple():
    for i in range(1, 21):
        dices = roll_dices(i)
        assert sum(histogram(dices, len(dices), i)) == i ** 2 + i


# Max subarray sum
def max_subarray_sum(t: array, n: int) -> int:
    histo = histogram(t, n)
    i_maximum = 6
    for i in range(6, 0, -1):
        if histo[i] > histo[i_maximum]:
            i_maximum = i
    return i_maximum * histo[i_maximum]


def test_max_subarray_sum():
    for i in range(1, 21):
        dices = roll_dices(i)
        histo = histogram(dices, len(dices))[1:]
        maxi = 6 - list(reversed(histo)).index(max(histo))
        assert max_subarray_sum(dices, len(dices)) == maxi * histo[maxi - 1]


# Move dices
def move_dices(t: array, n: int, value: int) -> array:
    margin = 0
    for i in range(n - 1, -1, -1):
        if value == t[i]:
            margin += 1
            continue
        t[i + margin] = t[i]
    for i in range(margin):
        t[i] = value
    return t


def test_move_dices():
    for i in range(1, 21):
        dices = roll_dices(i)
        value = random.randint(1, 7)
        number = number_of_dice_with_same_value(dices, len(dices), value)
        result = move_dices(dices, len(dices), value)
        assert result[:number] == array("H", [value] * number)
        assert all(dice != value for dice in result[number:])


# Roll dices again
def roll_dices_again(t: array, nt: int, s: array, ns: int) -> array:
    new_dices = roll_dices(ns)
    for i in range(ns):
        t[s[i]] = new_dices[i]
    return t


def test_roll_dices_again():
    for i in range(1, 21):
        dices = roll_dices(i)
        changes = array("H", [random.randint(0, i - 1) for _ in range(i)])
        for j, d in enumerate(
                roll_dices_again(dices, len(dices), changes, len(changes))
        ):
            if j not in changes:
                assert d == dices[j]


# Search sequence
def search_sequence(t: array, n: int):
    for r in range(2):
        v = r
        success = True
        for _ in range(n):
            v += 1
            s = False
            for i in range(n):
                if t[i] == v:
                    s = True
            if not s:
                success = False
                break
        if success:
            return r
    return -1


def test_search_sequence():
    for test in [
        {"dices": array("H", [6, 4, 2, 3, 5]), "should_result": 1},
        {"dices": array("H", [6, 4, 1, 3, 5]), "should_result": -1},
        {"dices": array("H", [4, 6, 3, 2, 5]), "should_result": 1},
        {"dices": array("H", [1, 2, 3, 4, 5]), "should_result": 0},
        {"dices": array("H", [2, 4, 1, 3, 5]), "should_result": 0},
    ]:
        dices = test.get("dices")
        should_result = test.get("should_result")
        assert search_sequence(dices, len(dices)) == should_result


# Play turn
def play_turn(n: int):
    dices = roll_dices(n)
    for tour_i in range(1, 4):
        histo = histogram(dices, n)
        i_max = 1
        for i in range(2, 7):
            if histo[i] >= histo[i_max]:
                i_max = i
        dices = move_dices(dices, n, i_max)
        print(f"Tirage {dices} tour {tour_i}")
        if histo[i_max] == histo[0]:
            print("YAMS!")
            break
        result = array("H", [0] * (n - histo[i_max]))
        for i in range(n - histo[i_max]):
            result[i] = i + histo[i_max]
        dices = roll_dices_again(dices, n, result, n - histo[i_max])
    return


if __name__ == "__main__":
    print("10: Round of play:")
    play_turn(5)
