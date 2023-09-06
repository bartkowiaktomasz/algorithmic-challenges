# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(nodes: List[int]):
    head = ListNode(nodes[0])
    prev = head
    for i in range(1, len(nodes)):
        n = ListNode(nodes[i])
        if i < len(nodes) and prev:
            prev.next = n
        prev = n
    return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        first = dummy
        
        for _ in range(left - 1):
        # "first" is the node to the left of the first one being reversed
            first = first.next
        # "tail" is the first one that is being reversed
        tail = first.next
        
        # The algorithm advances two pointers: first.next and tail.next
        #  at each iteration, increasing the reversed region
        #  e.g. revert between 2 and 4
        #  1 -> 2 -> 3 -> 4 -> 5
        #  f    t
        #  1 -> 3 -> 2 -> 4 -> 5
        #  f         t
        #  1 -> 4 -> 3 -> 2 -> 5
        #  f              t
        for _ in range(right - left):
            temp = first.next
            first.next = tail.next
            tail.next = tail.next.next
            first.next.next = temp

        return dummy.next
        

head = create_linked_list([3, 5])
sol = Solution()
res = sol.reverseBetween(head, 1, 2)
