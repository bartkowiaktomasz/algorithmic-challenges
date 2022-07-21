# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __repr__(self):
        return f"{self.val} -> {self.next}"

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        terminal = ListNode(-1, head)
        left = terminal
        while left.next and left.next.next:
            a = left.next
            b = left.next.next
            left.next, a.next, b.next = b, b.next, a
            left = a
        return terminal.next
            
sol = Solution()
a, b  = ListNode(1), ListNode(2)
a.next = b

print(
    sol.swapPairs(
        a
    )
)