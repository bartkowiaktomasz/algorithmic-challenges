# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(nodes: List[int]):
            if nodes:
                root = TreeNode(postorder.pop())
                root_idx = nodes.index(root.val)
                left, right = nodes[:root_idx], nodes[root_idx + 1:]
                root.right = build(right)
                root.left  = build(left)
                return root
            else:
                return None
        return build(inorder)
        