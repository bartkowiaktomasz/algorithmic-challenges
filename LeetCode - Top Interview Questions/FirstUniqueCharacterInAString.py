from collections import defaultdict

class DoublyLinkedListNode:
    def __init__(self, val: int):
        self.prev, self.next = None, None
        self.val = val

class Solution:
    def __repr__(self):
        ll = []
        node = self.start_node
        while node:
            ll.append(str(node.val))
            node = node.next
        return "->".join(ll)

    def firstUniqChar(self, s: str) -> int:
        start_node = DoublyLinkedListNode(-1)
        self.start_node = start_node
        terminal_node = DoublyLinkedListNode(-1)
        start_node.next, terminal_node.prev = terminal_node, start_node
        seen = dict()  # number -> node
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c not in seen:
                node = DoublyLinkedListNode(i)
                last = terminal_node.prev
                terminal_node.prev = node
                node.next = terminal_node
                last.next = node
                node.prev = last
                seen[c] = node
            else:
                if seen[c] is not None:
                    seen[c].prev.next = seen[c].next
                    seen[c].next.prev = seen[c].prev
                    seen[c] = None
        return terminal_node.prev.val

sol = Solution()
assert sol.firstUniqChar("leetcode") == 0
assert sol.firstUniqChar("loveleetcode") == 2
assert sol.firstUniqChar("aabb") == -1
assert sol.firstUniqChar("aadadaad") == -1