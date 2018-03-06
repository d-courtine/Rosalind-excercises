#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*
import sys
import os

n = 33+1
k = 5
pair_1 = 1
pair_2 = 0
pair_current = 0
first = True

for i in range(1, n):
    if first:
        first = False
    else:
        pair_current = pair_1 + (pair_2*k)
        pair_2 = pair_1
        pair_1 = pair_current
print(pair_current)

##### Found On Rosalind as solution #####
#def fib(n, k):  #n = month; k=number of rabbit pair per litter
#    a, b = 1, 1
#    for i in range(2, n):
#        a, b = b, k*a + b
#    return b
#
