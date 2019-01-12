"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
Calculate the sum of that subset.
"""

import os


def max(a, b, c):
    temp = a if a > b else b
    return temp if temp > c else c


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if (len(arr) == 1):
        return arr[0]
    elif (len(arr) == 2):
        return arr[0] if arr[0] > arr[1] else arr[1]

    n = len(arr)
    max_sum_arr = [None for _ in range(n)]
    max_sum_arr[0] = arr[0]
    max_sum_arr[1] = arr[0] if arr[0] > arr[1] else arr[1]

    for i in range(2, n):
        max_sum_arr[i] = max(arr[i], max_sum_arr[i - 1], arr[i] + max_sum_arr[i - 2])

    return max_sum_arr[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
