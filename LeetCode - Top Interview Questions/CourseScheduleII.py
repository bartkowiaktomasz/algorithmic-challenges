import copy
from collections import defaultdict, deque
from typing import List, Dict, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Use Kahn's algorithm (BFS falvour) to perform a toposort
        """
        edges_in = defaultdict(set)
        edges_out = defaultdict(set)
        # Courses without an incoming edge
        courses = set(range(numCourses))
        for a, b in prerequisites:
            edges_out[a].add(b)
            edges_in[b].add(a)
            if b in courses:
                courses.remove(b)
        toposort = deque()
        while courses:
            node = courses.pop()
            toposort.appendleft(node)
            edges_out_tmp = copy.copy(edges_out[node])
            for n in edges_out_tmp:
                edges_out[node].remove(n)
                edges_in[n].remove(node)
                if not edges_in[n]:
                    courses.add(n)
        if any(len(edges) for edges in edges_out.values()):
            return []
        return list(toposort)

sol = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(
    sol.findOrder(numCourses, prerequisites)
)