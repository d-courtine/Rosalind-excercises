#!/usr/bin/env python3
# -*- coding:utf-8 -*
import sys
#import os
#import math

###### Read in file

# f = open("test.txt", "r")
f = open("rosalind_ins.txt", "r")

toSort = f.readline().rstrip()
myList = f.readline().rstrip().split()
myList = [int(i) for i in myList]
# print("input:", myList)

# sys.exit()
num_swap = 0
for i in range(1, len(myList)):
    k = i
    while (k > 0) and (myList[k] < myList[k-1]):
        #swap the two positions
        t = myList[k-1]
        myList[k-1] = myList[k]
        myList[k] = t
        
        #step backward in case of the current number can be placed much before
        k = k - 1
        
        #Count the number of swap perfomed in total
        num_swap += 1

print("number of swap:", num_swap)    



#Algo
# for i = 2:n,
#     for (k = i; k > 1 and a[k] < a[k-1]; k--)
#         swap a[k,k-1]
#         k = k - 1
#   -> invariant: a[1..i] is sorted
#end


