# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast, start = head, head, True
        try:
            while start or slow is not fast:
                slow, fast = slow.next, fast.next.next
                start = False
        except AttributeError:
            return None
        slow = head
        while slow is not fast:
            slow, fast = slow.next, fast.next
        return slow