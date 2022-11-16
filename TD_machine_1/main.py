import random
from array import array


def roll_dices(n: int) -> array:
    result = array("H", [0]*n)
    for i in range(n):
        result[i] = random.randint(1, 6)
    return result


def sum_values(t: array, n: int) -> int:
    total = 0
    for i in range(n):
        total += t[i]
    return total


def number_of_dice_with_same_value(t: array, n: int, value: int) -> int:
    result = 0
    for i in range(n):
        if t[i] == value:
            result += 1
    return result


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


def max_subarray_sum(t: array, n: int) -> int:
    histo = histogram(t, n)
    i_maximum = 1
    for i in range(1, n + 2):
        if histo[i_maximum] <= histo[i]:
            i_maximum = i
    return i_maximum * histo[i_maximum]


def move_dice(t: array, n: int, value: int) -> array:
    margin = 0
    for i in range(n-1, -1, -1):
        if value == t[i]:
            margin += 1
            continue
        t[i+margin] = t[i]
    for i in range(margin):
        t[i] = value
    return t


def roll_dice_again(t: array, nt: int, s: array, ns: int) -> array:
    new_dices = roll_dices(ns)
    for i in range(ns):
        t[s[i]] = new_dices[i]
    return t


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


def jouer_tour(n: int):
    dices = roll_dices(n)
    for tour_i in range(1, 4):
        histo = histogram(dices, n)
        i_max = 1
        for i in range(2, 7):
            if histo[i] >= histo[i_max]:
                i_max = i
        dices = move_dice(dices, n, i_max)
        print(f"Tirage {dices} tour {tour_i}")
        if histo[i_max] == histo[0]:
            print("YAMS!")
            break
        result = array("H", [0]*(n-histo[i_max]))
        for i in range(n-histo[i_max]):
            result[i] = i+histo[i_max]
        dices = roll_dice_again(dices, n, result, n-histo[i_max])
    return


def main():
    n = 5

    dices = roll_dices(n)
    print(f"1: dices: {dices}")
    print(f"2: total: {sum_values(dices, n)}")
    print(f"3: number of '{dices[0]}': {number_of_dice_with_same_value(dices, n, dices[0])}")
    print(f"4: histogram: {histogram(dices, n)}")
    print(f"5: histogram with 5 launch: {histogram(dices, n, 5)}")
    print(f"6: max sum same dices: {max_subarray_sum(dices, n)}")
    print(f"7: move '6' dices: {move_dice(dices, n, 6)}")
    print(f"8: re roll index 4 and 5: {roll_dice_again(dices, n, array('H', [3, 4]), 2)}")
    print(f"9: search sequence: {search_sequence(dices, n)}")
    print("10: Round of play:")
    jouer_tour(n)


if __name__ == "__main__":
    main()
