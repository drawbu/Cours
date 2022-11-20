from array import array


def insert(t: array, n: int, elt: any, k: int) -> None:
    t.append(0)
    for i in range(n, k-1, -1):
        t[i] = elt if i == k else t[i-1]


def delete(t: array, n: int, k: int) -> None:
    for i in range(k, n):
        t[i] = t[i+1]


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


def max2(t: array, n: int):
    print(t, n)
    max_1 = max(t)
    max_2 = min(t)
    for i in range(n):
        print(i, t[i])
        if t[i] > max_1:
            max_2 = max_1
            max_1 = t[i]
            continue
        if t[i] > max_2:
            max_2 = t[i]
    return max_2


def deleteFirstInstance(t: array, n: int, elt: any):
    for i in range(n):
        if t[i] == elt:
            delete(t, n, i)
            return


def unduplicated(t, n):
    for i in range(n):
        occurence = 0
        for j in range(n):
            if t[i] == t[j]:
                occurence += 1
        if occurence > 1:
            return False
    return True


def tests():
    ...

if __name__ == "__main__":
    # # Exercice 2
    # t = array('b', list(range(10)))
    # print("\nExercice 2:")
    # print("  original:", list(t))
    # insert(t, 10, 12, 4)
    # print("  result:  ", list(t))

    # # Exercice 3
    # t = array('b', list(range(10)))
    # print("\nExercice 3:")
    # print("  original:", list(t))
    # delete(t, 9, 1)
    # print("  result:  ", list(t), "\n")

    # # Exercice 4
    # t = array('b', [2, 8, 11, 5, 9, 3, 1])
    # print("\nExercice 4:")
    # print("  original:     ", list(t))
    # print("  result with 7:", amplitude(t, 7))
    # print("  result with 4:", amplitude(t, 4))

    # # Exercice 5
    # t = array('b', [2, 8, 11, 5, 9, 3, 1])
    # print("\nExercice 5:")
    # print("  original:", list(t))
    # print("  result:  ", max2(t, 10),)

    # # Exercice 6
    # t = array('b', [10, 68, 78, 91, 68])
    # print("\nExercice 6:")
    # print("  original:", list(t))
    # deleteFirstInstance(t, 4, 68)
    # print("  result:  ", list(t))

    # Exercice 7
    t = array('b', [10, 68, 78, 91, 68])
    print("\nExercice 7:")
    print("  original:", list(t))
    print("  result:  ", unduplicated(t, 5))
