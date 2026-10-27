from code import Graph, UndirectedGraph, GraphAvecPoids


def construire_graphe():
    g = UndirectedGraph()
    g.addNodes(10)
    aretes = [
        (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (2, 5),
        (3, 4), (4, 5), (4, 6), (5, 6), (5, 7), (6, 7), (6, 9),
        (7, 8), (7, 9), (8, 9),
    ]
    for x, y in aretes:
        g.addEdge(x, y)
    return g


# a) Création impossible
try:
    Graph()
    print("Erreur, Graph() aurait dû échouer")
except NotImplementedError:
    print("Impossible de créer une instance")


# b) 10 nœuds et 17 arêtes
g = construire_graphe()
assert g.order() == 10
assert g.size() == 17
print("Ce test graphe avec 10 nœuds et 17 arêtes")


# c) recherche par identifiant
assert g.getNodeById(4).identifiant == 4
assert g.getNodeById(100) is None
print("Le test fonctionne, getNodeById fonctionne")

def construire_graphe_pondere():
    g = GraphAvecPoids()
    g.addNodes(6)
    aretes = [
        (0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15),
        (2, 3, 11), (2, 5, 2), (3, 4, 6), (5, 4, 9),
    ]
    for x, y, p in aretes:
        g.addEdge(x, y, p)
    return g


# d) 6 nœuds et 9 arêtes
w = construire_graphe_pondere()
assert w.order() == 6
assert w.size() == 9
print("Ce test graphe avec poids avec 6 nœuds et 9 arêtes")


# e) poids d'une arête (dirigée)
assert w.getPoids(0, 1) == 7.0
assert w.getPoids(1, 0) is None
print("Le test fonctionne, getPoids fonctionne")


# f) Dijkstra
assert w.dijkstra(0, 4) == (20.0, [0, 2, 5, 4])
assert w.dijkstra(4, 0) is None
print("Le test fonctionne, dijkstra fonctionne")