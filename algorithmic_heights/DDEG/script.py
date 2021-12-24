#!/usr/bin/env python3

import networkx as nx

#Read the graph with a package
# with open('test.txt', 'rb') as graph:
with open('rosalind_ddeg.txt', 'rb') as graph:
    graph_stats = next(graph).decode("utf-8").rstrip().split(' ') ## [0] = nb nodes, [1] = nb edges
    myGraph = nx.read_edgelist(graph)

"""
Return: An array D[1..n] where D[i] is the sum of the degrees of it's neighbour.
    1. browse the graph, and for each node, populate the dictionnary: {NodeID:[neighbourID]}
    2. browse the dictionnary, for each NodeID:
        - Get their neighbour
        - Sum their degrees.
"""

#setup the dictionary:
result = dict()
for node in range(1, int(graph_stats[0]) + 1):
    result[str(node)] = list()

# For each node, record it neighbour, in both direction
for edge in myGraph.edges():
    result[edge[0]].append(edge[1])
    result[edge[1]].append(edge[0])

# For each node, get the sum of the degrees of it's neighbour
for node, neighbour_list in result.items():
    degrees = 0
    for neighbour in neighbour_list:
        degrees += len(result[neighbour])
    print(degrees, end = ' ')
print()
