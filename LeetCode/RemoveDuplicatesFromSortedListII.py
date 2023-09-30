# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, cur = dummy, head
        while cur:
            runner = cur
            n_dups = -1
            while runner and runner.val == cur.val: runner = runner.next; n_dups += 1
            if n_dups > 0:
                prev.next = runner
            else:
                prev = cur
            cur = runner
        return dummy.next
        