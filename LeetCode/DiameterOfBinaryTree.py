# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        def longest_subpath(node: Optional[TreeNode]) -> int:
            nonlocal res
            if node is None:
                return 0
            left = longest_subpath(node.left)
            right = longest_subpath(node.right)
            res = max(res, left + right + 1)
            return left + 1 if left > right else right + 1
        longest_subpath(root)
        return res - 1
