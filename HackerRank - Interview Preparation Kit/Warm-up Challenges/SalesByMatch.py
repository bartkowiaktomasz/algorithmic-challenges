"""
Alex works at a clothing store. There is a large pile of socks that must be paired
by color for sale. Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

For example, there are `n=7` socks with colors `ar=[1,2,1,2,1,3,2]`.
There is one pair of color `1` and one of color `2`. There are three odd socks left,
one of each color. The number of pairs is `2`.
"""
from collections import Counter


def sockMerchant(n, ar):
    return sum([count // 2 for k, count in Counter(ar).items()])
