"""
You are given an array and you need to find number of tripets of indices
(i, j, k) such that the elements at those indices are in geometric progression
for a given common ratio r and i < j < k.
"""
from collections import defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    t2 = defaultdict(int)
    t3 = defaultdict(int)
    count = 0
    for elem in arr:
        if elem in t3:  # Check how many elements will form a triplet (i, j, elem)
            count += t3[elem]
        if elem in t2:  # Check how many elements will form a tuple (i, elem)
            # Add the number of those tuples to t3 as waiting
            #   for elem*r element to come and form a triple
            t3[elem*r] += t2[elem]
        t2[elem*r] += 1  # Increment the counter as this element is waiting for elem*r to form a tuple
    return count


# Test
l = map(int, "1 2 1 2 4".split(" "))
print(countTriplets(l, 2))
