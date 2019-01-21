"""
In this challenge, there is a connected undirected graph where each of the
nodes is a color. Given a color, find the shortest path connecting any two
nodes of that color. Each edge has a weight of 1. If there is not a pair or if
the color is not found, print -1.
"""

from collections import deque, defaultdict
import math
import os


class Graph(object):
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def add_edge(self, i, j):
        self.edges[i].append(j)
        self.edges[j].append(i)


# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def bfs(graph, start_node, nodes_colours, colour):
    visited = set()
    queue = deque()

    queue.append(start_node)
    visited.add(start_node)
    distance = 0
    while queue:
        node = queue.popleft()
        distance += 1
        for neighbour in graph.edges[node]:
            if not neighbour in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                if nodes_colours[neighbour - 1] == colour:
                    return distance

    return -1


def min_bfs(graph, nodes_colours, colour):
    nodes_of_required_colour = [i + 1 for i, col in enumerate(ids) if
                                col == colour]

    distances = [math.inf for _ in range(len(nodes_of_required_colour))]
    for i, node in enumerate(nodes_of_required_colour):
        distances[i] = bfs(graph, node, nodes_colours, colour)

    existing_distances = [dist for dist in distances if dist > 0]
    print(distances)
    if (len(existing_distances) == 0):
        return -1
    else:
        return min(existing_distances)


def build_graph(graph_nodes, graph_from, graph_to, ids):
    g = Graph(graph_nodes)
    for num, colour in enumerate(ids):
        g.edges[num + 1]

    for i, j in zip(graph_from, graph_to):
        g.add_edge(i, j)

    return g


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    g = build_graph(graph_nodes, graph_from, graph_to, ids)
    return min_bfs(g, ids, val)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    graph_nodes, graph_edges = map(int, input().split())
    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges
    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())
    ids = list(map(int, input().rstrip().split()))
    val = int(input())
    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    fptr.write(str(ans) + '\n')
    fptr.close()
