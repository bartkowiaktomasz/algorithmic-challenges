"""
You need to find the minimum number of swaps required to sort the array in
ascending order.
"""

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    d = {}
    min_swaps = 0
    sortedArr = sorted(arr)

    # Map element to its position in the sorted array (index from 1)
    # e.g. [3, 5, 6, 2, 4] => [2, 3, 4, 5, 6]
    # => d = {2 -> 0, 3 -> 1, 4 -> 2, 5 -> 3, 6 -> 4}
    for i, elem in enumerate(sortedArr):
        d[elem] = i

    # Add each element to the set
    # the elements will be then removed from it consecutively
    s = set()
    for elem in arr:
        s.add(elem)

    for elem in arr:
        if elem in s:
            if arr[d[elem]] == elem:
                # Element in the correct position
                s.remove(elem)
            else:
                cycle_length = 1
                i = elem
                while(arr[d[i]] != elem):
                    s.remove(i)
                    i = arr[d[i]]
                    cycle_length += 1
                min_swaps += cycle_length - 1
                s.remove(i)

    return min_swaps


arr_1 = """
2 31 1 38 29 5 44 6 12 18 39 9 48 49 13 11 7 27 14 33 50 21 46 23 15 26 8 47 40 3 32 22 34 42 16 41 24 10 4 28 36 30 37 35 20 17 45 43 25 19
"""
print(minimumSwaps(
    list(map(int, arr_1.split(" ")))
))
