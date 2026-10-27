class Node:
    def __init__(self, identifiant):
        self.identifiant = identifiant


class Graph:
    """Il s'agit d'une classe abstraite, on ne peut pas créer de Graph tout seul,
    il faut passer par une sous-classe."""
    def __init__(self):
        self.noeuds = {}
        self.aretes = {}
        raise NotImplementedError

    def addNode(self):
        """méthode concrète, il n'y a pas de paramètre, on cherche nous-même un
        identifiant libre avec une boucle, en testant à chaque
        fois qu'il n'est pas déjà utilisé par un autre nœud."""
        identifiant = 0
        while identifiant in self.noeuds:
            identifiant = identifiant + 1

        noeud = Node(identifiant)
        self.noeuds[noeud.identifiant] = noeud
        self.aretes[noeud.identifiant] = []

    def addNodes(self, nombre):
        """Il s'agit d'une méthode concrète concrète
        , on appelle simplement addNode() plusieurs fois"""
        for i in range(nombre):
            self.addNode()

    def addEdge(self, x, y):
        """Il s'agit d'une méthode abstraite dépend du type de graphe"""
        raise NotImplementedError

    def removeNode(self, noeud):
        """Il s'agit d'une méthode concrète, 
        on supprime uniquement les noeuds créés oar les méthodes addNode / addNodes"""

        if noeud in self.noeuds:
            del self.noeuds[noeud]
            del self.aretes[noeud]
            for autre in self.aretes:
                if noeud in self.aretes[autre]:
                    self.aretes[autre].remove(noeud)

    def removeEdge(self, x, y):
        """Méthode abstraite, elle dépend du type de graphe"""

        raise NotImplementedError

    def getNodeById(self, identifiant):
        """Il s'agti d'une méthode concrète car on supprime des noeuds pouvant être créés"""

        return self.noeuds.get(identifiant)

    def getNode(self, position):
        """Méthode concrète, il s'agit de la même chose"""

        liste = list(self.noeuds.values())
        if position < len(liste):
            return liste[position]
        return None

    def order(self):
        """Il s'agit d'une méthode concrète, l'ordre c'est juste le nombre de noeuds"""

        return len(self.noeuds)

    def size(self):
        """Méthode abstraite, la taille dépend du type de graphe (une arête est
        comptée deux fois dans un graphe non dirigé)"""

        raise NotImplementedError

    def density(self):
        """Méthode abstraite, la formule dépend du type de graphe"""

        raise NotImplementedError

    def getNeighbors(self, x):
        """Méthode concrète, les voisins de x sont dans la liste aretes[x]"""

        return self.aretes[x]

    def degree(self, x):
        """Méthode concrète, le degré c'est le nombre de voisins de x"""

        return len(self.aretes[x])

    def degreeDistribution(self):
        """Méthode concrète, on renvoie un dictionnaire {degré : nombre de noeuds}
        avec get(d, 0) pour commencer à 0 la première fois qu'on voit un degré"""

        distribution = {}
        for noeud in self.noeuds:
            d = self.degree(noeud)
            distribution[d] = distribution.get(d, 0) + 1
        return distribution


class UndirectedGraph(Graph):
    def __init__(self):
        """On ne rappelle pas Graph.__init__ sinon ça lève NotImplementedError"""

        self.noeuds = {}
        self.aretes = {}

    def addEdge(self, x, y):
        """Le graphe n'est pas dirigé donc on ajoute y chez x et x chez y"""

        self.aretes[x].append(y)
        self.aretes[y].append(x)

    def removeEdge(self, x, y):
        """On teste avant de supprimer (sinon remove() donne une erreur),
        et on supprime des deux côtés"""

        if y in self.aretes[x]:
            self.aretes[x].remove(y)
        if x in self.aretes[y]:
            self.aretes[y].remove(x)

    def size(self):
        """Chaque arête est dans la liste de x et dans celle de y,
        donc on divise le total par 2"""

        total = sum(len(v) for v in self.aretes.values())
        return total//2

    def density(self):
        """Formule du sujet : 2m / (n(n-1)). Si n<=1 on renvoie 0
        pour ne pas diviser par 0"""

        n = self.order()
        if n <= 1:
            return 0
        return (2*self.size()) / (n*(n - 1))

    def dfs(self, noeud, visite=None):
        """Parcours en profondeur récursif, la liste visite sert à ne pas
        passer deux fois sur le même noeud"""

        if visite is None:
            visite = []
        visite.append(noeud)
        for voisin in self.aretes[noeud]:
            if voisin not in visite:
                self.dfs(voisin, visite)
        return visite

    def IsConnected(self):
        """On fait un dfs depuis le premier noeud, si on visite tous les noeuds
        alors le graphe est connexe. Un graphe vide est considéré connexe"""
        
        if self.order() == 0:
            return True
        depart = list(self.noeuds.keys())[0]
        return len(self.dfs(depart)) == self.order()


class GraphAvecPoids(Graph):
    def __init__(self):
        """On ne rappelle pas Graph.__init__ sinon ça lève NotImplementedError,
        et on ajoute le dictionnaire des poids"""

        self.noeuds = {}
        self.aretes = {}
        self.poids = {}

    def addEdge(self, x, y, poids):
        """Méthode abstraite de Graph qu'on implémente avec un paramètre en plus.
        Le graphe est dirigé donc on ajoute seulement y chez x. On vérifie avec
        assert que les noeuds existent et que le poids n'est pas négatif. Si l'arête
        existe déjà on change juste son poids pour ne pas avoir deux arêtes x -> y"""

        assert x in self.noeuds and y in self.noeuds
        assert poids >= 0
        if y not in self.aretes[x]:
            self.aretes[x].append(y)
        self.poids[(x, y)] = float(poids)

    def removeEdge(self, x, y):
        """On supprime seulement x -> y (y -> x est une autre arête),
        en testant avant qu'elle existe et en enlevant aussi son poids"""

        if y in self.aretes[x]:
            self.aretes[x].remove(y)
            del self.poids[(x, y)]

    def removeNode(self, noeud):
        """On étend la méthode de Graph : on l'appelle d'abord pour supprimer
        le noeud et l'enlever des listes des autres, puis on refait le
        dictionnaire des poids sans les arêtes qui touchent ce noeud"""

        Graph.removeNode(self, noeud)
        nouveau = {}
        for (x, y) in self.poids:
            if x != noeud and y != noeud:
                nouveau[(x, y)] = self.poids[(x, y)]
        self.poids = nouveau

    def getPoids(self, x, y):
        """Renvoie le poids de x -> y, ou None si l'arête n'existe pas"""

        return self.poids.get((x, y))

    def size(self):
        """Chaque arête est stockée une seule fois dans poids (graphe dirigé),
        donc la taille c'est le nombre de poids"""

        return len(self.poids)

    def density(self):
        """Dans un graphe dirigé il y a n(n-1) arêtes possibles (et pas
        n(n-1)/2) donc la densité c'est m / (n(n-1)). Si n<=1 on renvoie 0"""

        n = self.order()
        if n <= 1:
            return 0
        return self.size() / (n * (n - 1))

    def dijkstra(self, source, cible):
        """Renvoie (distance, chemin), ou None si la cible est inaccessible.
        dist : distances trouvées (un noeud absent n'a pas encore été atteint).
        precedent : d'où on vient, pour reconstruire le chemin.
        restants : noeuds pas encore traités, on prend à chaque tour celui
        qui a la plus petite distance. On s'arrête quand c'est la cible."""

        assert source in self.noeuds and cible in self.noeuds
        dist = {source: 0.0}
        precedent = {}
        restants = list(self.noeuds.keys())

        while len(restants) > 0:
            courant = None
            for x in restants:
                if x in dist:
                    if courant is None or dist[x] < dist[courant]:
                        courant = x
            if courant is None or courant == cible:
                break
            restants.remove(courant)

            for voisin in self.aretes[courant]:
                nouvelle = dist[courant] + self.poids[(courant, voisin)]
                if voisin not in dist or nouvelle < dist[voisin]:
                    dist[voisin] = nouvelle
                    precedent[voisin] = courant

        if cible not in dist:
            return None

        chemin = [cible]
        while chemin[0] != source:
            chemin.insert(0, precedent[chemin[0]])
        return dist[cible], chemin