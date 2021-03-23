class Node:
    def __init__(self, key:int, val:int, next: 'TreeNode' = None, prev: 'TreeNode' = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
    
    def __repr__(self):
        return f"{self.key} ({self.val})"

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}  # key -> Node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        node = Node(key=key, val=value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            del self.cache[self.head.key]
            self._remove(self.head)
    
    def _add(self, node: Node):
        # Add node to the tail and change tail
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.tail.next = None
    
    def _remove(self, node: Node):
        prev = node.prev
        next_ = node.next
        if prev and next_:
            prev.next = next_
            next_.prev = prev
        elif not prev and not next_:
            self.head = None
            self.tail = None
        elif next_:  # no previous
            next_.prev = None
            self.head = next_
        else:  # no next
            prev.next = None
            self.tail = prev


def print_list(node):
    """
    Print linked list (for debugging purposes)
    """
    seen = set()
    while node:
        if not node in seen:
            seen.add(node)
        else:
            raise Exception
        print(f"({node.key}, {node.val}) -> ", end='')
        node = node.next
    print("None")

args = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

cache = LRUCache(args[0][0])
print(None)
for arg in args[1:]:
    if len(arg) == 1:  # get
        cache.get(arg[0])
    else:  # put
        cache.put(arg[0], arg[1])