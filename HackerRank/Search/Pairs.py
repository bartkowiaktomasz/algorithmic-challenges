"""
You will be given an array of integers and a target value.
Determine the number of pairs of array elements that have a difference
equal to a target value.
"""
import os

# Complete the pairs function below.
def pairs(k, arr):
    hash_map = {}
    for elem in arr:
        if elem not in hash_map:
            hash_map[elem] = 1
        else:
            hash_map[elem] += 1

    num_pairs = 0
    for elem in arr:
        elem_plus_k = elem + k
        elem_minus_k = elem - k

        if elem_plus_k in hash_map:
            num_pairs += hash_map[elem_plus_k]
        if elem_minus_k in hash_map:
            num_pairs += hash_map[elem_minus_k]

    return int(num_pairs / 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
