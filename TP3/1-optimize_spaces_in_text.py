def aligner_gauche_glouton(text: list[str], n: int, wpl: int) -> int:
    result = 0
    line = wpl - len(text[0])
    for i in range(1, n):
        if line - len(text[i]) < 1:
            result += line ** 3
            line = wpl
        else:
            line -= 1
        line -= len(text[i])
    return result


def aligner_gauche(text, n, N):
    c = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if n - i + sum_characters_words(text, n, i) <= N:
            c[i] = 0
            continue
        c[i] = 1e12
        for j in range(i, n):
            words_sum = sum_characters_words(text, j + 1, i)
            if (j - i) + words_sum <= N:
                if (N - j + i - words_sum) ** 3 + c[j + 1] < c[i]:
                    c[i] = (N - j + i - words_sum) ** 3 + c[j + 1]
    print(c)
    return c[0]


def sum_characters_words(text, n, i):
    if i >= n+1:
        return - 1

    somme = 0
    for j in range(i, n):
        somme += len(text[j])
    return somme


def tests():
    text = "En ouvrant un vieux coffret venu de l’Orient"
    text = text.split(" ")
    for i in range(20, 25):
        assert aligner_gauche_glouton(text, len(text), i) == aligner_gauche(text, len(text), i)
