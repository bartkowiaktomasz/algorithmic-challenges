"""
Given the head of a singly linked list, return true if it is a palindrome.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Idea: Revert the first half of the list and then iterate
        simultaneously with two pointers: one traverses from mid to start
        and the other one traverses from mid to end.
            e.g. 1 -> 2 -> 3 -> 2 -> 1 change to: 1 <- 2 <- 3 -> 2 -> 1
            e.g. 1 -> 2 -> 2 -> 1 change to: 1 <- 2  2 -> 1
        1. Use two pointers: slow, fast to find the mid of the list
        2. Iterate from the list start reversing its direction until we hit list's mid
        3. Iterate two pointers from mid, one towards the start, one towards the end
        to decide if palindrome
        """
        if head.next is None:
            # Linked list with one node is a palindrome
            return True
        len_ = 1   # Linked list is given to have least one node
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            len_ += 2
        if fast.next is not None:
            len_ += 1
        if len_ == 2:
            if head.val == head.next.val:
                return True
            else:
                return False
        # print(f"len of list is {len_}")
        # Now "slow" is either in the middle (odd number of nodes)
        # Or at the end of the first half of the list
        # Reverse first half of linked list (until "slow" pointer is hit)
        # e.g. 1 -> 2 -> 3 -> 2 -> 1 change to: 1 <- 2 <- 3 -> 2 -> 1
        # e.g. 1 -> 2 -> 2 -> 1 change to: 1 <- 2  2 -> 1
        # print(f"Slow: {slow.val}. fast: {fast.val}")
        left, mid, right = head, head.next, head.next.next
        # Use three pointers from the beginning to reverse linked list direction
        left.next = None
        while mid is not slow:
            mid.next = left
            left = mid
            mid = right
            right = right.next
        # Set up first, second pointers that traverse the list
        # mid-to-left and mid-to-right respectively
        if len_ % 2 == 0:
            mid.next = left
            first, second = mid, right
        else:
            first, second = left, right
        # print(f"first: {first.val}, second: {second.val}")
        while first is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

        
n1 = ListNode(3)
n2 = ListNode(3)
n3 = ListNode(1)
# n4 = ListNode(2)
# n5 = ListNode(1)
n1.next = n2
n2.next = n3
# n3.next = n4
# n4.next = n5

sol = Solution()
print(
    sol.isPalindrome(n1)
)
