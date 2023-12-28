# Definition for a binary tree node.
from collections import deque
from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbersIterative(self, root: Optional[TreeNode]) -> int:
        stack = deque([(root, 0)])
        sum_ = 0
        while stack:
            node, cur_sum = stack.pop()
            if node.left is None and node.right is None: sum_ += cur_sum + node.val
            else:
                if node.left is not None: stack.append((node.left, 10 * (cur_sum + node.val)))
                if node.right is not None: stack.append((node.right, 10 * (cur_sum + node.val)))
        return sum_

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_ = 0
        def dfs(node, cur_sum: int) -> Tuple[int, int, int]:
            nonlocal sum_
            if node.left is None and node.right is None:
                sum_ += cur_sum + node.val
            else:
                if node.left is not None: dfs(node.left, 10 * (cur_sum + node.val))
                if node.right is not None: dfs(node.right, 10 * (cur_sum + node.val))
        dfs(root, 0)
        return sum_