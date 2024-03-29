import copy
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(nodes: List[int]):
            if nodes:
                root = TreeNode(preorder.pop(0))
                root_idx = nodes.index(root.val)
                left, right = nodes[:root_idx], nodes[root_idx + 1:]
                root.left  = build(left)
                root.right = build(right)
                return root
            else:
                return None
        return build(inorder)