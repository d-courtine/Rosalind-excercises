#!/usr/bin/env python3

import networkx as nx

#Read the graph with a package
with open('test.txt', 'rb') as graph:
# with open('rosalind_deg.txt', 'rb') as graph:
    graph_stats = next(graph).decode("utf-8").rstrip().split(' ') ## [0] = nb nodes, [1] = nb edges
    myGraph = nx.read_edgelist(graph)

"""
Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.

1. browse the graph, and for each node, populate the dictionnary: {NodeID:[neighborID]}
2. browse the dictionnary, for each NodeID:
    - Get their neighbour
    - Sum their degrees.
"""

#setup the dictionary:
result = dict()
for node in range(1, len(myGraph.nodes()) + 1):
    result[str(node)] = list()

# Is there unconnected nodes?
if graph_stats[0] != len(result):
    print("There is at least a single node! %s %s" %(graph_stats[0], len(result)))

print(myGraph.nodes())

# for edge in myGraph.edges():
    # for node in edge:
    #     result[node] += 1
#
# [print(x, end = " ") for x in list(result.values())]
# print()

# print(result)
