from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __repr__(self):
        return f"{self.val}"

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        seen = dict()  # val -> node
        def dfs(node: Optional['Node'], clone: Optional['Node']):
            nonlocal seen
            if node.val not in seen:
                seen[node.val] = clone
                for n in node.neighbors:
                    if n.val in seen: c = seen[n.val]
                    else:
                        c = Node(n.val)
                    clone.neighbors.append(c)
                    dfs(n, c)
        root_clone = Node(node.val)
        dfs(node, root_clone)
        return root_clone

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

sol = Solution()
sol.cloneGraph(n1)