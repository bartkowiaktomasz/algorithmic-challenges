"""
Given `d` datasets, print the number of inversions that must be swapped to sort each dataset on a new line.
"""

import os

def merge(left, right, inversions):
    merged = []
    i, j = 0, 0
    while (i < len(left) and j < len(right)):
        # print("L, R: ", left, right)
        if (left[i] > right[j]):
            merged.append(right[j])
            j += 1
            inversions[0] += len(left) - i
        else:
            merged.append(left[i])
            i += 1
    if (i == len(left)):
        merged += right[j:]
        return merged
    else:
        merged += left[i:]
        return merged


def mergeSort(arr, inversions):
    if (len(arr) == 1):
        return arr
    else:
        mid = int(len(arr) / 2)
        left = arr[0:mid]
        right = arr[mid:]
        sortedArr = merge(mergeSort(left, inversions), mergeSort(right, inversions), inversions)
        return sortedArr


# Complete the countInversions function below.
def countInversions(arr):
    inversions = [0]
    mergeSort(arr, inversions)
    return inversions[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)
        fptr.write(str(result) + '\n')

    fptr.close()
