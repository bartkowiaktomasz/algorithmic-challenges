from collections import defaultdict
from typing import List, Set, Tuple

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.neigbours = []
    
    def __repr__(self) -> str:
        return str(self.val)
        

class Solution:
    def dfs(self, node: int, graph: List[List[int]], visited: Set[int]) -> bool:
        """
        Has cycle -> Return True
        State of "visited" list:
            0  - Not visited
            -1 - Currently being visited
            1  - Visited
        """
        if visited[node] == 1:
            return False
        if visited[node] == -1:
            return True
        visited[node] = -1
        has_cycle = any((visited[node] == -1 or self.dfs(node, graph, visited)) for node in graph[node])
        visited[node] = 1
        return has_cycle

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        a -> b means that "a" depends on "b", i.e. "b" is a prerequisite for "a"
        """
        graph = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        # 0 - Not visited, -1 - Currently being visited, 1 - Visited
        for course in range(numCourses):
            if visited[course] == 1:
                continue
            if self.dfs(course, graph, visited):
                return False
        return True

sol = Solution()
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(
    sol.canFinish(numCourses, prerequisites)
)