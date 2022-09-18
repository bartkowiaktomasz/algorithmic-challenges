from typing import Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def _visit(node: "TreeNode") -> Set:
            nonlocal res
            # Recurse first
            if node.left is not None:
                seen_left = _visit(node.left)
            else:
                seen_left = set()
            if node.right is not None:
                seen_right = _visit(node.right)
            else:
                seen_right = set()
            seen = seen_left.union(seen_right)
            # Then start updating nodes seen on the way up
            if node is p:
                seen.add(node)
            elif node is q:
                seen.add(node)
            if len(seen) == 2 and res is None:
                res = node
            return seen
        _visit(root)
        return res