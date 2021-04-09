# Definition for a Node.
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr:
            tmp = curr
            while tmp and tmp.left:
                tmp.left.next = tmp.right
                tmp.right.next = tmp.next.left if tmp.next else None
                tmp = tmp.next
            curr = curr.left
        return root
        