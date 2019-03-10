"""
You are given ``n`` queries, where each query consists of a map of HackerLand
and value of ``cost_library`` and ``cost_road``. For each query, find the minimum
cost of making libraries accessible to all the citizens and print it on a
new line.
"""

import os

def build_adjacency_list(n, cities):
    """Given list of lists (pairs of cities - edges) build an adjacency
    list for the graph"""
    _graph = dict()
    for i in range(n):
        _graph[i + 1] = list()
    for pair in cities:
        _graph[pair[0]].append(pair[1])
        _graph[pair[1]].append(pair[0])
    return _graph

def dfs(v, visited, vertices_in_component):
    """Returns the number of vertices in a given component"""
    visited.add(v)
    vertices_in_component.add(v)
    for n in graph[v]:  # "n" stands for "neighbour"
        if n not in visited:
            dfs(n, visited, vertices_in_component)
    return len(vertices_in_component)

def calculate_component_sizes(n, cities):
    """Given list of lists (pairs of cities - edges), compute the number
    of components in the graph"""
    global graph
    graph = build_adjacency_list(n, cities)
    component_sizes = list()
    visited = set()
    for v in list(graph.keys()):
        if v not in visited:
            size_of_component = dfs(v, visited, set())
            component_sizes.append(size_of_component)
    return component_sizes

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return c_lib * n
    else:
        component_sizes = calculate_component_sizes(n, cities)
        return c_lib*len(component_sizes) + sum([c_road * (size - 1) for size in component_sizes])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        nmC_libC_road = input().split()
        n = int(nmC_libC_road[0])
        m = int(nmC_libC_road[1])
        c_lib = int(nmC_libC_road[2])
        c_road = int(nmC_libC_road[3])
        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        fptr.write(str(result) + '\n')
    fptr.close()
