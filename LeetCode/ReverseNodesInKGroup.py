# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __repr__(self):
        return str(self.val)

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

def print_linked_list(head: ListNode):
    l = []
    while head:
        l.append(str(head.val))
        head = head.next
    return "->".join(l)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def _reverse_list(start: ListNode, stop: ListNode):
            if start is None or start is stop or start.next is None:
                return stop, start
            l, m, r = start, start.next, start.next.next
            l.next = None
            while m is not stop:
                m.next = l
                l, m = m, r
                r = r.next if (r is not None and r is not stop) else r
            m.next = l
            return stop, start  # stop == head, start == tail
        init = True
        start, stop, next_ = head, head, head
        prev_t = None
        while init or next_ is not None:
            i = 0
            while i < k:
                stop = next_
                next_ = next_.next
                i += 1
                if next_ is None:
                    break
            if i == k:
                h, t = _reverse_list(start, stop)
            else:
                h, t = start, stop
            if init:
                head = h
            if not init:
                prev_t.next = h
            start, stop, next_ = next_, next_, next_
            prev_t = t
            init = False
        return head
            
head = create_linked_list([1,2,3,4,5])
sol = Solution()
res = sol.reverseKGroup(head, k=2)
print(
    print_linked_list(res)
)