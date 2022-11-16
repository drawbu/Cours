def XSort(t, i, j):
    if i >= j:
        return
    XSort(t, i, j - 1)
    if t[j - 1] > t[j]:
        tmp = t[j - 1]
        t[j - 1] = t[j]
        t[j] = tmp
        XSort(t, i, j - 1)


if __name__ == "__main__":
    t = [3, 1, 2, 7, 8, 2]
    XSort(t, 0, 5)
    print(t)
