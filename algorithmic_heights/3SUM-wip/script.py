#!/usr/bin/env python3

"""
Given: A positive integer k≤20, a positive integer n≤10^4, and k arrays of size
n containing integers from −10^5 to 10^5.
Return: For each array A[1..n], output three different indices 1≤p<q<r≤n such
that A[p]+A[q]+A[r]=0 if exist, and "-1" otherwise.
"""

"""
IT CAN WORK THIS WAY, BUT the code has to test n * (n-1) * (n-2) combinations
for each array, which can be up to 9.10^11
"""


def check_qr(arr, p):
    indexes = None
    for q in range(p+1, len(arr)):
        for r in range(p+2, len(arr)):
            if (arr[p] + arr[q] + arr[r]) == 0:
                indexes = [p+1, q+1, r+1]
                break
        if indexes:
            break
    return indexes


def three_sum(arr):
    res = [-1]
    for p in range(0, len(arr)):
        # browse the array, and search for the array index with
        # the value == - p_value
        pqr = check_qr(arr, p)
        if pqr:
            res = pqr
            break
    return res


# with open("test.txt", "r" ) as f:
with open("rosalind_3sum.txt", "r") as f:
    next(f)
    lines = f.readlines()
    for line in lines:
        array = [int(x) for x in line.rstrip().split(' ')]

        # get the result as a list of str()
        result = list(map(str, three_sum(array)))

        print(" ".join(result))
