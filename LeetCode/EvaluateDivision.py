from typing import List

class Node:
    def __init__(self, val: str):
        self.val = None
        self.neighbors = {}  # neigbour (key) -> weight

class Solution:

    def __init__(self):
        self.nodes = {}  # val -> node

    def buildGraph(self, equations: List[List[str]], values: List[float]):
        for e, val in zip(equations, values):
            v = self.nodes.get(e[0], Node(e[0]))
            w = self.nodes.get(e[1], Node(e[1]))
            self.nodes[e[0]] = v
            self.nodes[e[1]] = w
            if e[1] in v.neighbors: continue  # same equation was processed already
            else:
                v.neighbors[e[1]] = val
                w.neighbors[e[0]] = 1/val

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(source: Node, cur: float) -> float:
            nonlocal visited, target
            if source is target: return cur
            for n in source.neighbors:
                node = self.nodes[n]
                if node not in visited:
                    visited.add(node)
                    val = dfs(node, cur * source.neighbors[n])
                    if val != -1: return val
                    visited.remove(node)
            return -1

        if not self.nodes: self.buildGraph(equations, values)
        res = []
        for v, w in queries:
            if v not in self.nodes or w not in self.nodes: val = -1
            else:
                visited = set()
                source, target = self.nodes[v], self.nodes[w]
                val = dfs(source, 1)
            res.append(val)
        return res
