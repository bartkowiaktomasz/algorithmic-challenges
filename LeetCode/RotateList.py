# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        head, tail = head, head
        list_len = 1
        while tail.next is not None:
            tail = tail.next
            list_len += 1
        k %= list_len
        if k == 0: return head
        new_tail, idx = head, 1
        # new tail should be at idx "list_len - k", counting from 1
        while idx < list_len - k:
            new_tail = new_tail.next
            idx += 1
        res = new_tail.next
        new_tail.next = None
        tail.next = head
        return res

