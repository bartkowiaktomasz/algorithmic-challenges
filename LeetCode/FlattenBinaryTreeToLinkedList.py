from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        left_val = self.left.val if self.left is not None else "#"
        right_val = self.right.val if self.right is not None else "#"
        return f"{self.val} (L: {left_val}, R: {right_val})"

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def solve(root: Optional[TreeNode]):
            if not root:
                return None
            right_rightmost = solve(root.right)
            left_rightmost = solve(root.left)

            if left_rightmost is not None:
                left_rightmost.right, root.right = root.right, root.left
            root.left = None
            return right_rightmost or left_rightmost or root.right or root
        solve(root)
        return root

def build_tree(nodes: List[int]) -> TreeNode:
    """Builds a tree one level at a time (left to right)

    Args:
        nodes (List[int]): List of node values, needs to be of length
            (exactly) 2^H - 1 (i.e. include `None` values to indicate no 
            children)

    Returns:
        TreeNode: root of the tree
    """
    nodes = [TreeNode(n) if n is not None else None for n in nodes]
    queue = deque([nodes[0]])
    i = 1
    while i < len(nodes):
        root = queue.popleft()
        left = nodes[i]
        right = nodes[i + 1] if i + 1 < len(nodes) else None
        root.left, root.right = left, right
        if left:
            queue.append(left)
        if right:
            queue.append(right)
        i += 2
    return nodes[0]

sol = Solution()
root = build_tree([1,2,None,3,None,4])
# root = build_tree([1,2,None,3])
res = sol.flatten(root)
root



