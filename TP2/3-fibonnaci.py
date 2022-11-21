from array import array
from timeit import timeit


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


def tests():
    for n, result in {0: 0, 2: 1, 5: 5, 7: 13, 9: 34, 15: 610}.items():
        assert fibo_recursive(n) == result
        assert fibo_iterative(n) == result


if __name__ == "__main__":
    tests()

    n_tests = 4_096
    n = 20


    def timer(func) -> float:
        return timeit(lambda: func(n), number=n_tests)


    print(f"With {n_tests:,} run for each:")
    print(f"fiboRecursive({n}): {timer(fibo_recursive):.2f}s")
    print(f"fiboIterative({n}): {timer(fibo_iterative):.2f}s")
