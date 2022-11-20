from array import array


def occurrence_max(t: array, n: int):
    n_plus_present = 0
    e_plus_present = -1
    for i in range(n):
        nbr = 0
        for j in range(i, n):
            if t[i] == t[j]:
                nbr += 1
        if nbr > n_plus_present:
            n_plus_present = nbr
            e_plus_present = t[i]
    return e_plus_present, n_plus_present


def sequence_max(t: array, n: int):
    sous_tableau_somme = t[0]
    for i in range(n):
        somme_for_i = 0
        for j in range(i, n):
            somme_for_i += t[j]
            if somme_for_i > sous_tableau_somme:
                sous_tableau_somme = somme_for_i
    return sous_tableau_somme



def tests():
    ...

if __name__ == "__main__":
    sentence = "l’élément le plus présent est {r[0]} avec {r[1]} occurrences."
    for t in (
        array("H", [0, 1, 4, 2, 3, 2, 2]),
        array("H", [6, 10, 6, 10, 7, 3]),
        array("H", [5, 8, 5, 5, 8, 8]),
    ):
        print(sentence.format(r=occurrence_max(t, len(t))))

    sentence = "la somme maximum est {r}"
    for t in (
            array("h", [0, -1, 2, -2, 3, 2]),
            array("h", [1, -10, 9, 6, 8, -6]),
            array("h", [6, 10, -6, -1, 7, 3]),
            array("h", [-4, 9, -3, -5, -8, 5]),
    ):
        print(sentence.format(r=sequence_max(t, len(t))))

