# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        init = True
        try:
            while True:
                if slow is fast and not init:
                    return True
                slow = slow.next
                fast = fast.next.next
                init = False
        except AttributeError:
            return False