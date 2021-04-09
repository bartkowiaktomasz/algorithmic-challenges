# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        headA_cp, headB_cp = headA, headB
        def get_len(head: ListNode):
            l = 0
            while head:
                l += 1
                head = head.next
            return l
        len_a, len_b = get_len(headA_cp), get_len(headB_cp)
        longer, shorter = (headA, headB) if len_a >= len_b else (headB, headA)
        len_longer, len_shorter = (len_a, len_b) if len_a >= len_b else (len_b, len_a)
        diff = len_longer - len_shorter
        for i in range(diff):
            longer = longer.next
        while shorter and longer and (shorter is not longer):
            shorter = shorter.next
            longer = longer.next
        if shorter is longer:
            return shorter
        return None
        
        