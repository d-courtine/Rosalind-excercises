#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*
import sys
import os
import networkx as nx

###### Read in file
f = open('test.txt', 'rb')
myGraph = nx.read_edgelist(f)


