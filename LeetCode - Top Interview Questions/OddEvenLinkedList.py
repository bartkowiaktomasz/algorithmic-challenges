from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        even, first_even = head.next, head.next
        # Even is in the front
        while odd.next and odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = first_even
        return head
        
nodes = [ListNode(n, None) for n in [1,2,3,4,5,6,7]]
# Set links
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
sol = Solution()
head = sol.oddEvenList(nodes[0])
i = 0
while i < 10 and head:
    print(head.val)
    head = head.next
    i += 1