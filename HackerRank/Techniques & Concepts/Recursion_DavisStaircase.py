import math
import os
import random
import re
import sys

def waysToClimb(n, waysToClimbArr):
    if(waysToClimbArr[n - 1] is not None):
        return waysToClimbArr[n - 1]
    else:
        waysToClimbArr[n - 4] = waysToClimb(n - 3, waysToClimbArr)
        waysToClimbArr[n - 3] = waysToClimb(n - 2, waysToClimbArr)
        waysToClimbArr[n - 2] = waysToClimb(n - 1, waysToClimbArr)
        return waysToClimb(n - 1, waysToClimbArr) + waysToClimb(n - 2, waysToClimbArr) + waysToClimb(n - 3, waysToClimbArr)

if __name__ == '__main__':
    s = int(input())

    for s_itr in range(s):
        n = int(input())
        waysToClimbArr = list()
        if(n < 3):
            waysToClimbArr = [None] * 3
        else:
            waysToClimbArr = [None] * n

        waysToClimbArr[0] = 1
        waysToClimbArr[1] = 2
        waysToClimbArr[2] = 4
        print(waysToClimb(n, waysToClimbArr))
