"""
Given an integer array of size , find the maximum of the minimum(s) of every
window size in the array. The window size varies from 1 to N.
"""

import os
from collections import deque, defaultdict


def idx_next_smaller(arr):
    stack = deque()  # stack of indices
    hashmap = dict()  # idx -> idx of the next smaller elem
    for i, elem in enumerate(arr):
        hashmap[i] = -1  # -1 means itself is the smallest
        if len(stack) == 0:
            stack.append(i)
        else:
            while len(stack) != 0 and arr[stack[-1]] > elem:
                top = stack.pop()
                hashmap[top] = i
            stack.append(i)
    out = [-1 for _ in range(len(arr))]
    for idx, idx_smaller in hashmap.items():
        out[idx] = idx_smaller
    return out


def next_smaller_dist(arr):
    """Compute distances to the next smaller element from given elem"""
    for i, elem in enumerate(arr):
        arr[i] = elem if elem == -1 else elem - i
    return arr


def max_window(arr):
    """Max size of window for which given index gives the smallest element
    in that window"""
    length = len(arr)
    # Distance to the smallest element to the right
    arr_l = next_smaller_dist(idx_next_smaller(arr))
    # Distance to the smallest element to the left
    arr_r = list(reversed(next_smaller_dist(idx_next_smaller(list(reversed(arr))))))
    max_windows = [0 for _ in range(length)]
    for i in range(length):
        if arr_l[i] == -1 and arr_r[i] == -1:
            max_windows[i] = len(arr_l)
        elif arr_l[i] == -1 and arr_r[i] != -1:
            max_windows[i] = (length - i) + (arr_r[i] - 1)
        elif arr_l[i] != -1 and arr_r[i] == -1:
            max_windows[i] = (i + 1) + (arr_l[i] - 1)
        else:
            max_windows[i] = (arr_l[i] - 1) + (arr_r[i] - 1) + 1
    return max_windows


# Complete the riddle function below.
def riddle(arr):
    max_windows = max_window(arr)
    hashmap = defaultdict(lambda: list())  # max_window -> list of elems
    for i in range(len(arr)):
        hashmap[max_windows[i]].append(arr[i])
    hashmap = dict(hashmap)
    min_max = [-1 for _ in range(len(arr))]
    # We know that the last element is of size of the whole array so this
    #   is the smallest element of the array
    min_max[-1] = min(arr)
    for i in reversed(range(1, len(arr))):
        try:
            max_i = max(hashmap[i])
            min_max[i - 1] = max(max_i, min_max[i])
        except KeyError:
            min_max[i - 1] = min_max[i]
    return min_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = riddle(arr)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
