# Definition for a binary tree node.
from collections import deque
import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Iterative
        """
        stack = deque([None])
        previous = None
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if previous and root and previous.val >= root.val:
                return False
            previous = root
            if root:
                root = root.right
        return True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive
        """
        def solve(node, min_, max_):
            if node is None: return True
            left_val = -math.inf if node.left is None else node.left.val
            right_val = math.inf if node.right is None else node.right.val
            if (left_val < node.val < right_val) and (min_ < node.val < max_):
                return solve(node.left, min_, node.val) and solve(node.right, node.val, max_)
            else: return False
        return solve(root, -math.inf, math.inf)