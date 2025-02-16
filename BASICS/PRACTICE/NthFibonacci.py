from math import *
from collections import *
from sys import *
from os import *

n = int(input())

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a,b = b, a + b
        return b

print(fibonacci(n))
## Read input as specified in the question.
## Print output as specified in the question.
