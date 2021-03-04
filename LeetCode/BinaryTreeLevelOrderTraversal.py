from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = deque([root])
        direction = 1
        while len(queue) > 0:
            single_res = []
            temp_queue = deque()
            while queue:
                node = queue.pop()
                if node is not None:
                    single_res.append(node.val)
                    if direction == 1:
                        temp_queue.appendleft(node.left)
                        temp_queue.appendleft(node.right)
                    else:
                        temp_queue.appendleft(node.right)
                        temp_queue.appendleft(node.left)
            direction *= -1
            queue = temp_queue
            if single_res:
                res.append(single_res)
        return res
        