# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None
        lt, geq = ListNode(-999), ListNode(-999)
        lt_head, geq_head = lt, geq
        while head:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                geq.next = head
                geq = geq.next
            head = head.next
        geq.next = None
        if lt_head.next is not None:
            lt.next = geq_head.next
            return lt_head.next
        else:
            return geq_head.next
            

def create_linked_list(nodes: List[int]):
    head = ListNode(nodes[0])
    prev = head
    for i in range(1, len(nodes)):
        n = ListNode(nodes[i])
        if i < len(nodes) and prev:
            prev.next = n
        prev = n
    return head

head = create_linked_list([1,4,3,2,5,2])
sol = Solution()
print(
    sol.partition(head, 3)
)