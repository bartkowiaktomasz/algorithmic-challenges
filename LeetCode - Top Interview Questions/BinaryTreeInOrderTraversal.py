from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = deque([None])
        while stack or root:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root:
                res.append(root.val) 
                root = root.right
        return res
        