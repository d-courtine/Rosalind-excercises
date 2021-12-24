#!/usr/bin/env python3

"""
Given: A positive integer k≤20, a positive integer n≤10^4, and k arrays of size n containing integers
from −10^5 to 10^5,
Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist,
and '-1' otherwise.
"""

def check(arr, p, pval):
    index = None
    for q in range(p+1, len(arr)):
        if pval == - arr[q]:
            #eg: 2 == - (-2) returns TRUE; while 2 == -(2) returns FALSE
            index = q
    return index

def two_sum(arr):
    res = [-1]
    for p in range(0, len(arr)):
        # browse the array, and search for the array index with the value == - p_value
        q = check(arr, p, arr[p])
        if q:
            res = [p+1, q+1]
            break
    return res

# with open("test.txt", "r" ) as f:
with open("rosalind_2sum.txt", "r" ) as f:
    next(f)
    lines = f.readlines()
    for line in lines:
        array = [int(x) for x in line.rstrip().split(' ')]
        result = list(map(str, two_sum(array))) #get the result as a list of str()

        print(" ".join(result))
