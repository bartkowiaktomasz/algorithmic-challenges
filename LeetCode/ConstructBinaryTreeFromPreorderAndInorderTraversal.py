import copy
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTreeRec(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Recursive solution
        """
        preorder = copy.copy(preorder)
        def build(inorder: List[int]):
            if inorder:
                val = preorder.pop(0)
                node = TreeNode(val)
                idx = inorder.index(val)
                left = inorder[0:idx]
                right = inorder[idx + 1 :]
                node.left = build(left)
                node.right = build(right)
                return node
            else:
                return None

        return build(inorder)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.buildTreeRec(preorder, inorder)