# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth, temp = -1, root
        while temp:
            depth += 1
            temp = temp.left
        # depth of root is 0
        # num nodes in the last level is between 0,...,2^depth
        # num nodes in the tree excl. last level is 2^depth - 1 (perfect tree)
        low, high = 0, int(2 ** depth)
        while low < high:
            mid = math.ceil(low + (high - low) / 2)
            dirs = bin(mid)[2:].zfill(depth)  # turns "mid" into binary e.g. "6" -> "110"
            node = root
            for d in dirs:
                node = node.left if d == "0" else node.right
            if node is not None: low = mid
            else: high = mid - 1
        # current "high" is the rightmost node in the last level
        return int((2 ** depth - 1)) + (high + 1)

root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.left, root.left.right, root.right.left = TreeNode(4), TreeNode(5), TreeNode(6)
sol = Solution()
print(
    sol.countNodes(root)
)