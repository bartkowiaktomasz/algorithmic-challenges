"""
Given the root of a binary search tree, and an integer `k`, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        last_val_seen = None
        num_unique_seen = 0
        res = None
        def traverse_in_order(node: TreeNode):
            nonlocal last_val_seen
            nonlocal num_unique_seen
            nonlocal res
            if node.left is not None:
                traverse_in_order(node.left)
            if node.val != last_val_seen:
                num_unique_seen += 1
            if num_unique_seen == k:
                res = node.val
                # Found a result, return immediately
                raise Exception
            last_val_seen = node.val
            if node.right is not None:
                traverse_in_order(node.right)
        try:
            traverse_in_order(root)
        finally:
            return res

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.right = TreeNode(2)

sol = Solution()
print(
    sol.kthSmallest(root, k=3)
)