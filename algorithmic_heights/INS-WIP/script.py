#!/usr/bin/env python3
# -*- coding:utf-8 -*
import sys
#import os
#import math

###### Read in file

f = open("test.txt", "r")

toSort = f.readline().rstrip()
myList = f.readline().rstrip().split()
myList = [int(i) for i in myList]

sys.exit()





#Algo
#for i = 2:n,
#    for (k = i; k > 1 and a[k] < a[k-1]; k--)
#        swap a[k,k-1]
#   -> invariant: a[1..i] is sorted
#end


