"""
File: unionFindCompare.py

Authors: Giovanni Pica, Amedeo Maria Paniccia, Francesco Legrottaglie

Modulo che contiene i confronti tra le tipologie di UnionFind
"""

from graph.algoritmi import *
from unionfind.quickFind import *
from time import time


def ufComparisons(G, N):
    start = time()
    qf = QuickFind()
    hasCycleUF(G, N, qf)
    end = time() - start
    print("QuickFind time->\t", end)

    start = time()
    qfb = QuickFindBalanced()
    hasCycleUF(G, N, qfb)
    end = time() - start
    print("QuickFindBalanced time->\t", end)

    start = time()
    qu = QuickUnion()
    hasCycleUF(G, N, qu)
    end = time() - start
    print("QuickUnion time->\t", end)

    start = time()
    qub = QuickUnionBalanced()
    hasCycleUF(G, N, qub)
    end = time() - start
    print("QuickUnionBalanced time->\t", end)

    start = time()
    qubps = QuickUnionBalancedPathSplitting()
    hasCycleUF(G, N, qubps)
    end = time() - start
    print("QuickUnionBalancedPathSplitting time->\t", end)

    start = time()
    qubpc = QuickUnionBalancedPathCompression()
    hasCycleUF(G, N, qubpc)
    end = time() - start
    print("QuickUnionBalancedPathCompression time->\t", end)


if __name__ == "__main__":

    for i in range(1000,10001,1000):
        # con cicli
        print("\ngrafo con almeno un ciclo:\n")
        print("numero nodi",i)
        G=GraphAdjacencyList()
        graphCycle(G,i)
        ufComparisons(G, i)

        # senza cicli
        # print("grafo senza cicli:\n")
        # print("numero nodi",i)
        # G=GraphAdjacencyList()
        # graphNOcycle(G,i)
        # ufComparisons(G,i)