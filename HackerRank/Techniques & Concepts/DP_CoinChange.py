import math
import os
import random
import re
import sys

def coinChange(n, m, coins):
    tempStorage = [[-1 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(n + 1):
        tempStorage[0][i] = 0
    for i in range(m + 1):
        tempStorage[i][0] = 1

    for row in range(1, m + 1):
        for value in range(1, n + 1):
            # The answer is a sum of two mutually exclusive cases:
            # 1. Get the sum without usin the new coin (row)
            # 2. Get the sum with using new coin
            # Add those two sums together
            if(value >= coins[row - 1]):
                tempStorage[row][value] = tempStorage[row - 1][value] + tempStorage[row][value - coins[row - 1]]
            else:
                tempStorage[row][value] = tempStorage[row - 1][value]

    return tempStorage[m][n]

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    coins = list(map(int, input().rstrip().split()))
    print(coinChange(n, m, coins))
