import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    minAbsoluteDiff = abs(arr[1] - arr[0])
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < minAbsoluteDiff:
            minAbsoluteDiff = abs(arr[i] - arr[i + 1])
            print("min abs diff changed to ", minAbsoluteDiff)

    return minAbsoluteDiff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
