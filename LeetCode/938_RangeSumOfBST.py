# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_ = 0
        def solve(node):
            nonlocal sum_
            if node is None: return
            if low <= node.val <= high:
                sum_ += node.val
            if low <= node.val: solve(node.left)
            if high >= node.val: solve(node.right)
        solve(root)
        return sum_
        