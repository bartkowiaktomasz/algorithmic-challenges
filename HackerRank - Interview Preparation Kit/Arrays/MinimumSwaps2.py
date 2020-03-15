"""
You need to find the minimum number of swaps required to sort the array in
ascending order.
"""
import os

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    d = {}
    min_swaps = 0
    sortedArr = sorted(arr)

    # Map element to its position in the sorted array (index from 1)
    for i, elem in enumerate(sortedArr):
        d[elem] = i + 1

    # Add each element to the set
    # the elements will be then removed from it consecutively
    s = set()
    for elem in arr:
        s.add(elem)

    for elem in arr:
        if(elem in s):
            if arr[d[elem] - 1] == elem:
                s.remove(elem)
            else:
                cycle_length = 1
                i = elem
                while(arr[i - 1] != elem):
                    s.remove(i)
                    i = arr[i - 1]
                    cycle_length += 1
                min_swaps += cycle_length - 1
                s.remove(i)

    return min_swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
