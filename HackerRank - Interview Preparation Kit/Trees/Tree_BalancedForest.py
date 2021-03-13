"""
Solve in `O(n)` using DFS. For each node keep track (`Counter`) of subtree
sums (cumulative) seen above it (up to the root) and below it 
(another `Counter`). Use DFS to traverse all edges, considering, for each 
edge, whether it can be cut or not. It can be cut when one of four cases is met.
"""

from typing import List, Set, Dict
from collections import Counter

class TreeNode:
    def __init__(self, val: int = -1):
        self.val = val
        self.parent = None
        self.children = []
        self.subtree_sum = -1
        self.neighbours = []
    
    def __repr__(self):
        return f"{self.val}"

# Complete the balancedForest function below.
def balancedForest(c, edges):
    nodes = [TreeNode(val) for val in c]
    # Establish neighbours in the graph
    for edge in edges:
        i, j = (edge[0] - 1, edge[1] - 1)
        nodes[i].neighbours.append(nodes[j])
        nodes[j].neighbours.append(nodes[i])
        
    # Build a tree with BFS with nodes[0] being a root
    queue = set([nodes[0]])
    visited = set()
    while queue:
        current = queue.pop()
        visited.add(current)
        for node in current.neighbours:
            if node not in visited:
                node.parent = current
                current.children.append(node)
                queue.add(node)
    
    subtree_sums_counter = Counter()
    def calcCumSum(node: TreeNode):
        """
        Calculate subtree sums for each node. Subtree sum includes the value
        of a given node
        """
        if not node.children:
            node.subtree_sum = node.val
            subtree_sums_counter[node.subtree_sum] += 1
            return node.val
        else:
            node.subtree_sum = sum([calcCumSum(child) for child in node.children]) + node.val
            subtree_sums_counter[node.subtree_sum] += 1
            return node.subtree_sum
    calcCumSum(nodes[0])
    total_sum = nodes[0].subtree_sum
    res = float('inf')
    def solve(node: TreeNode, sums_seen_below: Dict[int, int], sums_seen_above: Dict[int, int]):
        """
        Solve by considering each edge once using DFS (recurisvely)
        Once found an answer, update the value of "res".
        
        There are four cases when an edge can be cut - see inline comments
        """
        nonlocal res
        sums_seen_above[node.subtree_sum] += 1
        for child in node.children:
            sums_seen_below_child = Counter()
            solve(child, sums_seen_below_child, sums_seen_above)
            sums_seen_below += sums_seen_below_child
        sums_seen_above[node.subtree_sum] -= 1
        sums_seen_below[node.subtree_sum] += 1
        # 1. Current subtree has the same size as some other subtree
        # Cut at current node, there is another subtree somewhere with the same
        #  subtree sum and the root subtree, after two cuts, is smaller
        diff = total_sum - 2 * node.subtree_sum
        if (
            subtree_sums_counter[node.subtree_sum] > (sums_seen_above[node.subtree_sum] + sums_seen_below[node.subtree_sum])
            and node.subtree_sum >= diff
        ):
            res = min(res, node.subtree_sum - diff)
        # 2. Current subtree has the same size as some other subtree
        # Cut at current node, if we subtract twice the current subtree sum
        #  from the root node we some hypothetical third subtree - check if it exists
        #  and see if it's smaller than the current subtree
        diff = total_sum - 2 * node.subtree_sum
        if (
            subtree_sums_counter[diff] > sums_seen_below[diff]
            and node.subtree_sum - diff >= 0
        ):
            res = min(res, node.subtree_sum - diff)
        # 3. Current subtree is smaller than two other, equal subtrees
        # Cut at current node, the root node can then be divided into two
        #  equal subtrees which are bigger than the current subtree
        diff = (total_sum - node.subtree_sum) / 2
        if (
            subtree_sums_counter[diff] > sums_seen_below[diff]
            and subtree_sums_counter[diff] > sums_seen_above[diff]
            and diff - node.subtree_sum >= 0
        ):
            res = min(res, diff - node.subtree_sum)
        # 4. Current subtree is bigger that the root with the rest
        # Do a cut inside such that one of the subtrees has the same size as root
        diff = (total_sum - node.subtree_sum)
        if (
            node.subtree_sum >= diff
            and (sums_seen_below[node.subtree_sum - diff] > 0 or sums_seen_below[diff] > 0)
        ):
            if diff - (node.subtree_sum - diff) >= 0:
                res = min(res, diff - (node.subtree_sum - diff))
    solve(nodes[0], Counter(), Counter())
    return -1 if res == float('inf') else int(res)


c_raw = "7 7 21 3 1 2"
edges_raw = """1 2
3 1
2 4
5 2
2 6"""
c = list(map(int, c_raw.split(" ")))
edges = [list(map(int, edge.split(' '))) for edge in edges_raw.split('\n')]
print(
    balancedForest(c, edges)
)
    