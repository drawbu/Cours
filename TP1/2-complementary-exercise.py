def number_sections(t, nt, s, ns):
    results = 0
    for i in range(nt - ns):
        valid = 0
        for j in range(ns):
            if s[j] == t[i + j]:
                valid += 1
        if valid == ns:
            results += 1
    return results


def test_number_sections():
    assert number_sections([5, 1, 2, 3, 1, 2, 1], 7, [1, 2], 2) == 2
    assert number_sections([5, 1, 2, 1, 2, 1], 6, [1, 2, 1], 2) == 2
