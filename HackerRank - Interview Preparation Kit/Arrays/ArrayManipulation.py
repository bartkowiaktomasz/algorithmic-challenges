"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation
add a value to each of the array element between two given indices, inclusive.
Once all operations have been performed, return the maximum value in the array.
"""

import os

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    initial = [0 for _ in range(n)]
    for query in queries:
        initial[query[0] - 1] += query[2]
        if(query[1] < n):
            initial[query[1]] -= query[2]
    sum = 0
    max = sum
    for elem in initial:
        sum += elem
        if(sum > max):
            max = sum
    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
