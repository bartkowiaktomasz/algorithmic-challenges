# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validateRec(self, root: TreeNode) -> bool:
        """
        Recursive version
        """
        left = root.left
        right = root.right
        def validate(left, right) -> bool:
            if left is not None and right is not None:
                if left.val == right.val:
                    return validate(left.left, right.right) and validate(left.right, right.left)
                else:
                    return False
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
        return validate(left, right)
    
    def validateIter(self, root: TreeNode) -> bool:
        """
        Iterative version
        """
        queue = deque()
        queue.append(root.right)
        queue.append(root.left)
        while queue:
            i = queue.pop()
            j = queue.pop()
            if i is None and j is None:
                continue
            if i is None or j is None:
                return False
            if i.val != j.val:
                return False
            queue.append(i.right)
            queue.append(j.left)
            queue.append(i.left)
            queue.append(j.right)
        return True
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        return self.validateIter(root)