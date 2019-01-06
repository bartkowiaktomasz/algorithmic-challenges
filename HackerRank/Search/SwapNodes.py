#!/bin/python3

import os
import sys

sys.setrecursionlimit(15000)  # to pass two last cases

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = -1
        self.right = -1
        self.visited = False
        self.level = -1


"""
Build a tree using queue.
Return the root of the tree and a hashmap with all nodes.
"""
def buildTree(indexes):
    queue = deque()
    nodemap = {}
    root = Node(1)
    root.level = 1
    nodemap[1] = root
    queue.append(root)
    for pair in indexes:
        parent = queue.popleft()
        if pair[0] != -1:
            value = pair[0]
            parent.left = Node(value)
            parent.left.level = parent.level + 1
            nodemap[value] = parent.left
        if pair[1] != -1:
            value = pair[1]
            parent.right = Node(value)
            parent.right.level = parent.level + 1
            nodemap[value] = parent.right
        if parent.left != -1:
            queue.append(parent.left)
        if parent.right != -1:
            queue.append(parent.right)

    return root, nodemap


"""
For each swap query we need to traverse the tree in order,
so the graph needs to be cleared (all nodes changed to unvisited)
"""
def resetVisitedNodes(nodemap):
    for _, value in nodemap.items():
        value.visited = False


"""
Swap children of all nodes at appropriate depth.
"""
def swap(root, nodemap, query):
    for _, node in nodemap.items():
        if node.level % query == 0:  # if its child is at appropriate depth
            print("Swapping children of node ", node.value)
            temp = node.left
            node.left = node.right
            node.right = temp

    out = printInOrder(root)
    resetVisitedNodes(nodemap)
    return out


def printInOrder_recursive(node, out):
    if node.left != -1:
        printInOrder_recursive(node.left, out)

    if not node.visited:
        node.visited = True
        out.append(node.value)

    if node.right != -1:
        printInOrder_recursive(node.right, out)


"""
Initialise an empty output array and append to it recursively
in printInOrder_recursive function
"""
def printInOrder(node):
    out = []
    printInOrder_recursive(node, out)  # append to output array
    return out


#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    root, nodemap = buildTree(indexes)
    out = []
    for query in queries:
        out.append(swap(root, nodemap, query))
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    indexes = []
    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))
    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)
    result = swapNodes(indexes, queries)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()
