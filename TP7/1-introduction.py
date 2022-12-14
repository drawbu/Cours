from bibgraphes import (
    ouvrirGraphe,
    afficherGraphe,
    sommetNom,
    listeVoisins,
    colorierSommet,
    listeSommets,
    __c_node,
    __c_graph,
    degre,
    marquerSommet,
    demarquerSommet,
    estMarqueSommet,
)


def color_neighbours(node: __c_node, color: str) -> None:
    for neighbour in listeVoisins(node):
        colorierSommet(neighbour, color)


def test_color_neighbours():
    graphe = ouvrirGraphe("./TP7/graphes/tgv.dot")
    node = sommetNom(graphe, "Bordeaux")
    color_neighbours(node, "yellow")
    for n in listeVoisins(node):
        assert n.color == "yellow"


def number_edges(graphe: __c_graph) -> int:
    n = 0
    for node in listeSommets(graphe):
        n += degre(node)
    return n // 2


def test_number_edges():
    assert number_edges(ouvrirGraphe("./TP7/graphes/complet.dot")) == 10
    assert number_edges(ouvrirGraphe("./TP7/graphes/europe.dot")) == 30
    assert number_edges(ouvrirGraphe("./TP7/graphes/graphe1.dot")) == 7
    assert number_edges(ouvrirGraphe("./TP7/graphes/tgv.dot")) == 20


def is_simple(graphe: __c_graph) -> bool:
    for node in listeSommets(graphe):
        checked_neighbours = []
        for neighbour in listeVoisins(node):
            if node.label == neighbour.label:
                return False
            if neighbour.label in checked_neighbours:
                return False
            checked_neighbours.append(neighbour.label)
    return True


def test_is_simple():
    assert is_simple(ouvrirGraphe("./TP7/graphes/tgv.dot"))
    assert not is_simple(ouvrirGraphe("./TP7/graphes/graphe1.dot"))


def improved_is_simple(graphe: __c_graph) -> bool:
    for node in listeSommets(graphe):
        for neighbour in listeVoisins(node):
            if node.label == neighbour.label:
                return False
            if estMarqueSommet(neighbour):
                return False
            marquerSommet(neighbour)
        for neighbour in listeVoisins(node):
            marquerSommet(neighbour)
    return True


def test_improved_is_simple():
    assert is_simple(ouvrirGraphe("./TP7/graphes/tgv.dot"))
    assert not is_simple(ouvrirGraphe("./TP7/graphes/graphe1.dot"))
