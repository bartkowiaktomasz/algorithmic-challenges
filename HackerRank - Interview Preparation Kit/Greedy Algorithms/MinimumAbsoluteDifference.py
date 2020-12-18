"""
Given an array of integers, find and print the minimum absolute difference between
any two elements in the array.
"""


def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    minAbsoluteDiff = abs(arr[1] - arr[0])
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < minAbsoluteDiff:
            minAbsoluteDiff = abs(arr[i] - arr[i + 1])

    return minAbsoluteDiff

