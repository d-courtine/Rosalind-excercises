#!/usr/bin/env python3

import networkx as nx

#Read the graph with a package
# with open('test.txt', 'rb') as graph:
with open('rosalind_deg.txt', 'rb') as graph:
    next(graph) # we do not need this line ==> nbr of nodes and edges
    myGraph = nx.read_edgelist(graph)

#setup the dictionary:
result = dict()
for node in range(1, len(myGraph.nodes()) + 1):
    result[str(node)] = 0

for edge in myGraph.edges():
    for node in edge:
        result[node] += 1

[print(x, end = " ") for x in list(result.values())]
print()
