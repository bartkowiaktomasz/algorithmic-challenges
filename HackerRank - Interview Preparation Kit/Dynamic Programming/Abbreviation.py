"""
You can perform the following operations on the string, a:
1. Capitalize zero or more of a's lowercase letters.
2. Delete all of the remaining lowercase letters in a.
Given two strings, a and b, determine if it's possible to make  equal to  as
described. If so, print YES on a new line. Otherwise, print NO.
"""

import os
import sys

sys.setrecursionlimit(2000)


# Complete the abbreviation function below.
def abbreviation_recursive(a, b, memo):
    idx_a = len(a) - 1
    idx_b = len(b) - 1
    if (idx_a, idx_b) in memo:
        return memo[(idx_a, idx_b)]
    # if both are empty
    if not a and not b:
        memo[(idx_a, idx_b)] = "YES"
        return "YES"
    # if a is empty and b is not
    if b and not a:
        memo[(idx_a, idx_b)] = "NO"
        return "NO"
    # if b is empty and a is only lowercase
    if not b and a.lower() == a:
        memo[(idx_a, idx_b)] = "YES"
        return "YES"
    # if b is empty and a is not only lowercase
    if not b and a.lower() != a:
        memo[(idx_a, idx_b)] = "NO"
        return "NO"

    last_a = a[-1]
    last_b = b[-1]

    if last_a == last_b:
        return abbreviation_recursive(a[:-1], b[:-1], memo)
    if last_a.lower() == last_b.lower():
        bool_one = abbreviation_recursive(a[:-1], b, memo) == "YES"
        if bool_one:
            memo[(idx_a, idx_b)] = "YES"
            return "YES"
        else:
            bool_two = abbreviation_recursive(a[:-1], b[:-1], memo) == "YES"
            if bool_two:
                memo[(idx_a, idx_b)] = "YES"
                return "YES"
            else:
                memo[(idx_a, idx_b)] = "NO"
                return "NO"
    if last_a.lower() == last_a:
        return abbreviation_recursive(a[:-1], b, memo)

    memo[(idx_a, idx_b)] = "NO"
    return "NO"


def abbreviation(a, b):
    memo = {}
    return abbreviation_recursive(a, b, memo)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        fptr.write(result + '\n')
    fptr.close()
