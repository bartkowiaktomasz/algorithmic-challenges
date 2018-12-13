"""
Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?
"""
import os

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices_sorted = sorted(prices)
    toys = 0
    for price in prices_sorted:
        if(price <= k):
            k -= price
            toys += 1
        else:
            return toys

    return toys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()
