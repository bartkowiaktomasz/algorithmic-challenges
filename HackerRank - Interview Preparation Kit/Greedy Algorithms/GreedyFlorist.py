"""
Minimize the amount of money it costs for a group of friends to
buy all 'n' flowers
"""

import os


# Complete the getMinimumCost function below.
def getMinimumCost(k, cost_arr):
    sorted_cost_arr = sorted(cost_arr)
    arr_ptr = len(cost_arr) - 1
    min_cost = 0
    num_round = 0
    while arr_ptr >= 0:
        for i in range(k):
            if arr_ptr >= 0:
                min_cost += sorted_cost_arr[arr_ptr] * (1 + num_round)
            else:
                return min_cost
            arr_ptr += -1
        num_round += 1
    return min_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    fptr.write(str(minimumCost) + '\n')
    fptr.close()
