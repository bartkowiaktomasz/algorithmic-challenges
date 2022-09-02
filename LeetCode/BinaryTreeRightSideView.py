# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        curr_level = deque([root])
        next_level = deque()
        res = []
        while curr_level:
            node = curr_level.popleft()
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
            if not len(curr_level):
                res.append(node.val)
                curr_level = next_level
                next_level = deque()
        return res

        