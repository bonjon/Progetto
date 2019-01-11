"""
File: decorator.py

Authors: Giovanni Pica, Amedeo Maria Paniccia, Francesco Legrottaglie

Modulo che contiene l'implementazione del decorator per confrontare i due algoritmi
"""

from graph.algoritmi import *
def timer(func):
    """
    Decorator che calcola il tempo di esecuzione della funzione e quantifica il numero di archi presenti nel grafo
    al variare della dimensione
    :param func:
    :return: funzione di wrap
    """
    def wrapping_function(**kwargs):
        for i in range(1000, 10001, 1000):
            start = time()
            value=func(i, **kwargs)  # chiamata alla funzione da decorare
            elapsed = time() - start
            print(f'Function {func.__name__} with {value} edges took {elapsed} seconds')
    return  wrapping_function


@timer
def testUf(N):
    G=GraphAdjacencyList()
    graphCycle(G,N)
    #graphNOcycle(G,N)
    hasCycleUF(G,N,QuickUnion())
    i=len(G.getEdges())
    return i
@timer
def testDfs(N):
    G = GraphAdjacencyList()
    graphCycle(G, N)
    #graphNOcycle(G,N)
    hasCycleDFS(G)
    i = len(G.getEdges())
    return i



if __name__ == "__main__":
    print("UNIONFIND\n")
    testUf()
    print("\n------------------------------------------------------------------\n")
    print("DFS\n")
    testDfs()

