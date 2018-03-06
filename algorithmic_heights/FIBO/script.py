#!/Users/courtine/anaconda3/bin/python
# -*- coding:utf-8 -*

##### Quick way ####
#def fibonacci(n):
#    a, b = 0, 1
#    for i in range(0, n+1):
#        a, b = b, a + b
#    return a


def fib_func(n):
    fib = []
    for i in range(1, n+1):
        if i == 1:
            fib = [0, 1]
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib[-1]

print(fib_func(24))
