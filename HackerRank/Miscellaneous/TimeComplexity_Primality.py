import math
import os
import random
import re
import sys

def isPrime(n):
    if(n == 1):
        return 'Not prime'
    if(n == 2):
        return 'Prime'
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if(n % i == 0):
            return 'Not prime'
    return 'Prime'

if __name__ == '__main__':
    p = int(input())

    for p_itr in range(p):
        n = int(input())
        print(isPrime(n))
