"""
The kingdom of Zion has cities connected by bidirectional roads. There is a
unique path between any pair of cities. Morpheus has found out that the machines
are planning to destroy the whole kingdom. If two machines can join forces,
they will attack. Neo has to destroy roads connecting cities with machines in
order to stop them from joining forces. There must not be any path connecting
two machines.

Each of the roads takes an amount of time to destroy, and only one can be
worked on at a time. Given a list of edges and times, determine the minimum
time to stop the attack.

TLDR: Given a graph with green and red nodes and weighted edges, define
the edges with the least cost that, when removed, result in disjoint graphs
that have at max one red node.
"""


class Node:
    """
    Node object implementing Union-Find (a.k.a DisjointSet) functionality
    with Path compression.
    """
    # Map value to a corresponding Node object
    map_ = dict()

    def __init__(self, value: int):
        self.value = value
        self.parent = self
        self.rank = 0
        self.has_machine = False  # Machine == red node
        Node.map_[value] = self

    def union(self, v: 'Node'):
        node_u = self
        node_v = v

        root_u = node_u
        while root_u.parent is not root_u:
            root_u = root_u.parent

        root_v = node_v
        while root_v.parent is not root_v:
            root_v = root_v.parent

        if root_u is root_v:
            return

        # Whoever has a higher rank becomes a parent
        # If ranks are equal, increment the rank of the parent
        if node_u.rank >= node_v.rank:
            Node.join_compress(node_v, node_u)
            node_v.parent = node_u
            if node_u.rank == node_v.rank:
                node_u.rank += 1
        else:
            Node.join_compress(node_u, node_v)
            node_u.parent = node_v

    def find(self) -> 'Node':
        running = self
        original_node = running  # To use later for path compression
        while not running.parent is running:
            running = running.parent

        Node.join_compress(original_node, running)
        return running

    @staticmethod
    def join_compress(child: 'Node', parent: 'Node'):
        temp = child
        while temp.parent is not parent:
            next = temp.parent
            temp.parent = parent
            temp = next


def minTime(roads, machines):
    machines_set = set(machines)
    # Sort roads by decreasing weight
    roads_sorted = sorted(roads, key=lambda r: r[2], reverse=True)
    time = 0
    for r in roads_sorted:
        u, v, t = r
        node_u = Node(u) if u not in Node.map_ else Node.map_[u]
        node_v = Node(v) if v not in Node.map_ else Node.map_[v]

        if node_u.value in machines_set:
            node_u.find().has_machine = True

        if node_v.value in machines_set:
            node_v.find().has_machine = True

        if not node_u.find().has_machine and not node_v.find().has_machine:
            node_u.union(node_v)
        elif node_u.find().has_machine and node_v.find().has_machine:
            time += t
        else:
            node_u.union(node_v)
            node_u.find().has_machine = True
    return time


roads = """2 1 8
1 0 5
2 4 5
1 3 4"""

machines = """2
4
0"""

roads = [list(map(int, r.split())) for r in roads.split("\n")]
machines = list(map(int, machines.split("\n")))

print(
    minTime(
        roads, machines
    )
)
