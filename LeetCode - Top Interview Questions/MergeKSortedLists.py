"""
You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
# Definition for singly-linked list.
import itertools
from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}"


class Solution:
    counter = itertools.count()

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        node_queue = []
        root_node = ListNode(float("inf"))
        for node in lists:
            if not node:
                continue
            heapq.heappush(
                # Value, counter object (to tie equal priorities), Node object
                node_queue, (node.val, next(self.counter), node)
            )
        previous_node = root_node
        while node_queue:
            (val, _, current_node) = heapq.heappop(node_queue)
            if val == float("inf"):
                break
            previous_node.next = current_node
            previous_node = current_node
            if current_node.next is None:
                new = ListNode(float("inf"))
                heapq.heappush(
                    node_queue,
                    (new.val, next(self.counter), new)
                )
            else:
                heapq.heappush(
                    node_queue, (current_node.next.val, next(self.counter), current_node.next)
                )
        return root_node.next


def _print_node(node: ListNode):
    if node:
        while node.next:
            print(node.val)
            node = node.next
        print(node)


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = [[]]
lists_nodes = [[ListNode(i) for i in l] for l in lists]
for l in lists_nodes:
    for i in range(len(l) - 1):
        l[i].next = l[i + 1]

s = Solution()
_print_node(s.mergeKLists([l[0] for l in lists_nodes]))
