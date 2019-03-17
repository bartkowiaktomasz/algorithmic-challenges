"""
You will be given a list of integers, ``arr``, and a single integer ``k``.
You must create an array of length ``k`` from elements of ``arr`` such that its
unfairness is minimized. Call that array ``subarr``. Unfairness of an array is
calculated as ``max(subarr) - min(subarr)``
"""


# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)
    min_diff = arr[k - 1] - arr[0]
    for i in range(len(arr) - k + 1):
        diff = arr[i + k - 1] - arr[i]
        min_diff = diff if diff < min_diff else min_diff
    return min_diff


# Test
arr = [100, 200, 300, 350, 400, 401, 402]
print(maxMin(3, arr))  # Expected: 2
