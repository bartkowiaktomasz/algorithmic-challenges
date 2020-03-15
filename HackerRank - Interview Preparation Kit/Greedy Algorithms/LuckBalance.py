#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    sortedContests = sorted(contests, key=lambda x: x[0], reverse=True)
    luck = 0
    for contest in sortedContests:
        if contest[1] == 0:
            luck += contest[0]
        else:
            if k > 0:
                luck += contest[0]
                k += -1
            else:
                luck -= contest[0]

    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()
