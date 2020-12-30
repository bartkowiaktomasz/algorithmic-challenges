# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = head
        j = head
        prev = head
        x = 1
        while x < n:
            i = i.next
            x += 1
        while i.next is not None:
            prev = j
            i = i.next
            j = j.next

        if j is head:
            # There is no previous node
            return head.next
        if n == 1:
            # There is no next node
            prev.next = None
            return head
        else:
            prev.next = j.next
            return head
