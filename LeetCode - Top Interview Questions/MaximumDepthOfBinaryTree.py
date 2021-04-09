# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepthIter(self, root: TreeNode) -> int:
        """
        Iterative solution using BFS
        """
        if not root:
            return 0
        max_depth = 1
        stack = deque([(root, max_depth)])
        while stack:
            root, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if root.left:
                stack.append((root.left, depth + 1))
            if root.right:
                stack.append((root.right, depth + 1))
        return max_depth
            
    
    def maxDepthRec(self, root: TreeNode) -> int:
        """
        Recursive solution
        """
        if not root:
            return 0
        max_depth = 1
        def solve(root: TreeNode, depth: int):
            nonlocal max_depth
            if not root:
                return
            max_depth = max(max_depth, depth)
            solve(root.left, depth + 1)
            solve(root.right, depth + 1)
        solve(root, max_depth)
        return max_depth
    
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepthIter(root)