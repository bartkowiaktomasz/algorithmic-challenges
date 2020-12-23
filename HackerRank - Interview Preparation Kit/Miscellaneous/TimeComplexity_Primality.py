"""
A prime is a natural number greater than `1` that has no positive divisors other than
`1` and itself. Given `p` integers, determine the primality of each integer and return
`Prime` or `Not prime` on a new line.
"""

import math


def isPrime(n):
    if(n == 1):
        return 'Not prime'
    if(n == 2):
        return 'Prime'
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if(n % i == 0):
            return 'Not prime'
    return 'Prime'

s = """30
1
4
9
16
25
36
907"""
l = list(map(int, s.split("\n")))
print(
    list(map(isPrime, l))
)
