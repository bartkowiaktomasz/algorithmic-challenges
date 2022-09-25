from collections import defaultdict, deque
from email.policy import default
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes: List[int]) -> TreeNode:
    """Builds a tree given a list of nodes one level at a time (left to right)

    Args:
        nodes (List[int]): List of node values

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

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = defaultdict(int)  # path_lengths -> count
        cache[0] = 1
        res = 0
        def dfs(root, cur_sum):
            nonlocal cache, res
            if root is None:
                return
            cur_sum += root.val
            res += cache[cur_sum  - targetSum]
            cache[cur_sum] += 1
            dfs(root.left, cur_sum)
            dfs(root.right, cur_sum)
            cache[cur_sum] += -1

        dfs(root, 0)
        return res

# Example 1
root2, target2 = build_tree([10,5,-3,3,2,None,11,3,-2,None,1]), 8
root3, target3 = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22
root4, target4 = build_tree([1,None,2,None,3,None,4,None,5]), 3
root5, target5 = build_tree([1]), 0
root6, target6 = build_tree([1,-2,-3]), -1


sol = Solution()
assert sol.pathSum(root2, target2) == 3
assert sol.pathSum(root3, target3) == 3
assert sol.pathSum(root4, target4) == 2
assert sol.pathSum(root5, target5) == 0
assert sol.pathSum(root5, target5) == 0
assert sol.pathSum(root6, target6) == 1
