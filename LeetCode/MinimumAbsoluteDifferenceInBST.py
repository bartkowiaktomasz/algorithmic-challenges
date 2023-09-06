# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        def inorder(root: Optional[TreeNode]) -> List[int]:
            nonlocal vals
            if root is None:
                return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        inorder(root)
        return min([abs(vals[i + 1] - vals[i]) for i in range(len(vals) - 1)])
        

            
        