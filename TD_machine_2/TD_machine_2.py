from random import randint
from array import array
from timeit import timeit
import numpy as np


def sum_int(n: int, i: int = 1):
    if i == n:
        return i
    return i + sum_int(n, i + 1)


def sum_array(t: array, n: int):
    if n == 1:
        return t[n - 1]
    return t[n - 1] + sum_array(t, n - 1)


def one_complement(t: array, n: int):
    if n == 0:
        return t
    if t[n - 1] == 1:
        t[n - 1] = 0
    else:
        t[n - 1] = 1
    return one_complement(t, n - 1)


def reverse(t, n, i=0):
    if n == 1:
        return t[n - 1]
    return t[n - 1] + reverse(t, n - 1, i)


def sum_array2(t: array, n: int, i: int = 0):
    if i == n - 1:
        return t[i]
    return t[i] + sum_array2(t, n, i + 1)


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


def prime_number(n: int, i: int = 0):
    if (n % (i + 2)) == 0:
        if i + 2 == n:
            return True
        return False
    return prime_number(n, i + 1)


def fraction_egyptienne2(a, b, t, i=0):
    ...


def fibo_recursive(n):
    if n in (0, 1):
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def fibo_iterative(n):
    results = array("H", [0] * (n + 1))
    for i in range(n + 1):
        if i in (0, 1):
            results[i] = i
            continue
        results[i] = results[i - 1] + results[i - 2]
    return results[n]


class Labyrinthe:
    def __init__(self):
        self.labyrinthe = np.array([[1] * 4] * 4)
        self.labyrinthe[2][0] = 0
        self.labyrinthe[1][1] = 0
        print(self.look_neighbourhood(2, 2))

    def look_neighbourhood(self, x, y):
        for neighbour_x in range(4):
            for neighbour_y in range(4):
                print(neighbour_x, neighbour_y)

    def __repr__(self):
        return "\n" + "\n".join(" ".join(map(str, e)) for e in self.labyrinthe)


def tests():
    ...


if __name__ == "__main__":
    test_timeit = False

    print("Une série de petits exercices")
    print(f"1. sumInt(5): {sum_int(5)}")
    tab = [randint(0, 10) for _ in range(3)]
    print(f"2. sumArray({tab}, 5):", sum_array(array("H", tab), 3))
    print(
        f"3. oneComplement([1,1,1,0], 4): {one_complement(array('i', [1, 1, 1, 0]), 4)}")
    print(
        f"4. reverse(['p','e','t','i','t'], 5): {reverse(array('u', ['p', 'e', 't', 'i', 't']), 5)}")
    print(
        f"5. sum_array2([2, 3, -1, 4], 4, 1): {sum_array2(array('i', [2, 3, -1, 4]), 4)}")
    print(
        f"6. is_sorted([1, 2, 3, 7], 4): {is_sorted(array('H', [1, 2, 3, 7]), 4)}")
    print(
        f"   is_sorted([1, 2, 3, 2], 4): {is_sorted(array('H', [1, 2, 3, 2]), 4)}")
    print(f"7. pair(3): {pair(3)}")
    print(f"8. maximum({tab}, 3): {maximum(array('H', tab), 3)}")
    print(f"9. primeNumber(7): {prime_number(7)}")
    print(f"   primeNumber(8): {prime_number(8)}")

    print("\nRetour sur la fraction égyptienne")
    print(
        f"  fraction_egyptienne2(3, 5, [0]*10, 0): {fraction_egyptienne2(3, 5, array('l', [0] * 10))}")

    print(f"\nLa suite de Fibonacci")
    print(f"  fiboRecursive(4): {fibo_recursive(4)}")
    print(f"  fiboIterative(4): {fibo_iterative(4)}")
    if test_timeit:
        print("  Timing :")
        print(f"    fiboRecursive(8): {timeit(lambda: fibo_recursive(8)):.2f}s")
        print(f"    fiboIterative(8): {timeit(lambda: fibo_iterative(8)):.2f}s")

    print(f"\nLabyrinthe")
    print(f"  labyrinthe(): {Labyrinthe()}")
