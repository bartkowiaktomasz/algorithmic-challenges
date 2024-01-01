# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            res.append(queue[-1].val)
            new_queue = deque()
            while queue:
                node = queue.popleft()
                if node.left is not None: new_queue.append(node.left)
                if node.right is not None: new_queue.append(node.right)
            queue = new_queue
        return res