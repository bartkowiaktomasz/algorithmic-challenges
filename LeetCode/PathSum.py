# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def solve(node: TreeNode, curSum: int) -> bool:
            if node is None: return False
            elif node.left is None and node.right is None and (curSum + node.val) == targetSum: return True
            elif node.left is None and node.right is None and (curSum + node.val) != targetSum: return False
            else: return solve(node.left, curSum + node.val) or solve(node.right, curSum + node.val)
        return solve(root, 0)