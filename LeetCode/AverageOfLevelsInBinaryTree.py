# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs = []
        stack = [root]
        while stack:
            i, sum_, new_stack = 0, 0, []
            while stack:
                node = stack.pop()
                sum_ += node.val
                i += 1
                if node.left is not None: new_stack.append(node.left)
                if node.right is not None: new_stack.append(node.right)
            avgs.append(sum_ / i)
            stack = new_stack 
        return avgs
        