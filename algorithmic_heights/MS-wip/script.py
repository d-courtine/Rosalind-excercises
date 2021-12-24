#!/usr/bin/env python3


def factorial(n):
    print("n =", n)

    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

print(factorial(5))

"""
To read:
https://www.tutorialspoint.com/python_data_structure/python_divide_and_conquer.htm
"""
#
# with open(test.txt, r) as f:
#     next(f)
#     array = f.readline().rstrip().split(' ')
#     array = list(map(int, array))
#
#     print(array)
#
