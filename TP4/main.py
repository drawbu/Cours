from random import randint as rd
from timeit import timeit
from array import array


def XSort(t: array, i: int, j: int) -> None:
    if i >= j:
        return
    XSort(t, i, j - 1)
    if t[j - 1] > t[j]:
        tmp = t[j - 1]
        t[j - 1] = t[j]
        t[j] = tmp
        XSort(t, i, j - 1)


def main():
    def timer(func, *argv) -> str:
        return f"{timeit(lambda: func(*argv), number=1):.2f}s"

    for i in range(7):
        arr = [None] * (10 ** i)
        for j in range(10 ** i):
            arr[j] = rd(0, 10)
        print(f"{10 ** i}: {timer(XSort, arr, 0, len(arr) - 1)} -> {arr}")


if __name__ == "__main__":
    main()
