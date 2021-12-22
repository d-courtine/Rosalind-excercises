#!/usr/bin/env python3

# ROSALIND - Majority element
"""
An array A[1..n] is said to have a majority element if more than half of its entries are the same.
Given: A positive integer k≤20, a positive integer n≤10^4, and k arrays of size n containing positive integers not exceeding 10ˆ5
Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and -1 otherwise.
"""
import collections

def majorityElement(nums):
    mid_value = len(nums)//2
    counts = collections.Counter(nums) # get a dict with key = element; value = # of occurences of the element
    max_occurence = 0
    max_key = ""
    for k,v in counts.items(): # Search for the key with the highest number of occurences
        if v > max_occurence:
            max_occurence = v
            max_key = k
    if max_occurence <= mid_value: # filter on the nunber of occurences
        max_key = -1
    return max_key

# with open('test.txt', 'r') as f:
with open('rosalind_maj.txt', 'r') as f:
    next(f) #we don't need this line
    lines = f.readlines()
    results = list()
    for line in lines:
        table = line.rstrip().split(' ')
        #convert str to int
        table = list(map(int, table))
        print(majorityElement(table), end = " ")

print()
