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
        # In-order traversal using stack
        stack = []
        cur = root
        i = 1
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if i == k: return cur.val
            cur = cur.right
            i += 1
        return -1

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