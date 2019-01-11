"""
File:algoritmi.py

Authors: Giovanni Pica, Amedeo Paniccia, Francesco Legrottaglie

Modulo che contiene l'implementazione di hasCycleUF & hasCycleDFS, iterator per scandire gli archi & algoritmo
che crea grafi con o senza cicli
"""

from graph.Graph_AdjacencyList import *
from unionfind.quickUnion import *
from datastruct.Stack import PilaArrayList as Stack
from time import time
from random import randint


class iterEdge:

    def __init__(self, E):
        print("\n^^^ARCHI^^^\n")
        self.a = E

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.a) == 0:
            raise StopIteration
        else:
            b = self.a
            self.a = self.a[1:]
            return b[0]


def hasCycleUF(G, N, uf):
    visited = []  # in visited mettiamo gli archi che visiteremo
    E = G.getEdges()
    for i in range(N):  # facciamo il makeSet
        uf.makeSet(i)
    for j in E:  # scorriamo tutti gli archi in E(G) non visitati
        if str(j) not in visited:
            u = uf.nodes[int(str(j.tail))]  # nodo da dove inizia l'arco
            v = uf.nodes[int(str(j.head))]  # nodo dove finisce
            if (uf.find(u) == uf.find(v)):
                return 1
            else:
                uf.union(uf.findRoot(u), uf.findRoot(v))
                arcoUV = str(G.getEdge(int(str(j.tail)), int((str(j.head)))))
                arcoVU = str(G.getEdge(int(str(j.head)), int((str(j.tail)))))
                visited.append(arcoUV)
                visited.append(arcoVU)
    return 0


def hasCycleDFS(G):
    for rootId in G.getNodes():

        dfs_nodes = []  # qui è dove metteremo i Nodi Chiusi

        # Inizializziamo la pila dove inseriamo i Nodi Aperti
        s = Stack()
        s.push(rootId.id)

        explored = {rootId.id}  # nodi visitati

        while not s.isEmpty():  # finchè ci sono nodi da esplorare ...
            node = s.pop()  # prendiamo il nodo dalla pila
            explored.add(node)  # marchiamo il nodo
            # aggiungiamo tutti i nodi adiacenti non esplorati nella pila
            for i in range(len(G.getAdj(node)) - 1, -1, -1):
                adj_node = G.getAdj(node)[i]
                if adj_node not in explored:
                    explored.add(adj_node)
                    s.push(adj_node)
                elif s.inPila(adj_node):  # se il nodo adiacente è un nodo aperto allora abbiamo un ciclo!
                    return 1
            dfs_nodes.append(node)
        return 0


def graphCycle(graph, N):
    list_nodes = []
    for i in range(N):
        node = graph.addNode(i)
        list_nodes.append(node)
    for node_src in list_nodes:  # un ciclo
        if node_src.id < len(list_nodes) - 1:
            graph.insertEdge(node_src.id, list_nodes[node_src.id + 1].id)
            graph.insertEdge(list_nodes[node_src.id + 1].id, node_src.id)
    b = randint(0, len(list_nodes) - 3)
    graph.insertEdge(len(list_nodes) - 1, b)
    graph.insertEdge(b, len(list_nodes) - 1)


def graphNOcycle(graph, N):
    list_nodes = []
    for i in range(N):
        node = graph.addNode(i)
        list_nodes.append(node)
    for node_src in list_nodes:  # nessun ciclo!
        if node_src.id < len(list_nodes) - 1:
            graph.insertEdge(node_src.id, list_nodes[node_src.id + 1].id)
            graph.insertEdge(list_nodes[node_src.id + 1].id, node_src.id)
        else:
            break


if __name__ == "__main__":
    graph = GraphAdjacencyList()
    uf = QuickUnion()
    N = 10000

    # grafo con almeno un ciclo

    graphCycle(graph, N)
    graph.print()
    print("\nTempi Algoritmi:")
    start1 = time()
    hasCycleDFS(graph)
    elapsed = time() - start1
    print("tempo DFS->\t\t\t", elapsed)

    start = time()
    hasCycleUF(graph, N, uf)
    end = time() - start
    print("tempo UNIONFIND->\t", end)
    print("\n\n")

    E = list(str(i) for i in graph.getEdges())

    for c in iterEdge(E):
        print("EDGE{}".format(c))

    # grafo senza cicli

    graph2 = GraphAdjacencyList()
    uf2 = QuickUnion()
    graphNOcycle(graph2, N)
    graph2.print()
    print("\nTempi Algoritmi:")

    start1 = time()
    hasCycleDFS(graph2)
    elapsed = time() - start1
    print("tempo DFS->\t\t\t", elapsed)

    start2 = time()
    hasCycleUF(graph2, N, uf2)
    end2 = time() - start2
    print("tempo UNIONFIND->\t", end2)
    print("\n\n")

    E = list(str(i) for i in graph2.getEdges())

    for c in iterEdge(E):
        print("EDGE{}".format(c))
