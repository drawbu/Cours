from array import array


def fusion(t1: array, n1: int, t2: array, n2: int, t3: array) -> array:
    for (t, n) in ((t1, n1), (t2, n2)):
        for i in range(n):
            for j in range(n1+n2):
                if t[i] > t3[j]:
                    for k in range(n1+n2-1, j, -1):
                        t3[k] = t3[k-1]
                    t3[j] = t[i]
                    break


if __name__ == "__main__":
    t1 = array("H", [2, 5, 5, 8, 9])
    t2 = array("H", [1, 3, 5])
    t3 = array("H", [0]*(len(t1)+len(t2)))
    fusion(t1, len(t1), t2, len(t2), t3)
    print(t3)
