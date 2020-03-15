import queue
from collections import defaultdict

class Graph(object):
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, x):
        distances = [-1 for i in range(self.n)]
        unvisitedNodes = set([i for i in range(self.n)])
        q = queue.Queue()

        distances[x] = 0
        unvisitedNodes.remove(x)
        q.put(x)

        while not q.empty():
            u = q.get()
            for neighbour in self.edges[u]:
                if neighbour in unvisitedNodes:
                    distances[neighbour] = distances[u] + 6
                    unvisitedNodes.remove(neighbour)
                    q.put(neighbour)

        for i, dist in enumerate(distances):
            if (i != x):
                print(dist, end=" ")
        print()


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)