from typing import Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val}"


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        Bottom-up merge sort. Merge sublists of size step = 1, 2, 4, ..., n
        Example: Say a step is 2 and the list is 4 -> 2 -> 1 -> 3 -> [tail of the list]
        1. Cut a list into smaller sublist 4 -> 2 -> None and save a pointer to 
            the next element (-> 1)
        2. Make another cut to get 1 -> 3 -> None and save a pointer to the remainder
            of the list (to be sorted in the next iteration) as `cur`
        3. Merge 4 -> 2 and 1 -> 3 with regular merge operation. Merge operation
            returns the first element of merged list (1) and the last node (4)
        4. Append sorted list to already sorted part of the list (`tail` node)
        5. Update the tail to be the last sorted element (4)
        
        """
        if not head or not head.next:
            return head

        n = self.getListLength(head)
        dummy = ListNode('-inf', next=head)
        step = 1
        while step < n:
            cur = dummy.next
            tail = dummy
            while(cur):
                left = cur
                right = self.split_cut(left, step)
                cur = self.split_cut(right, step)
                first, last = self.merge(left, right)
                tail.next = first
                tail = last
            step *= 2
        return dummy.next

    def merge(self, left: ListNode, right: ListNode) -> Tuple[ListNode, ListNode]:
        """
        Merge two linked lists and return first and last node of merged list
        """
        dummy = ListNode('-inf')
        head = dummy
        while left and right:
            if left.val <= right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        head.next = right if not left else left
        while head:
            prev = head
            head = head.next
        prev.next = None
        return dummy.next, prev

    def split_cut(self, head: ListNode, step: int) -> ListNode:
        """
        Given an input linked list, get `step` nodes from it and make a "cut"
        e.g. 
        head = 4 -> 2 -> 1 -> 3, step = 2 gives:
        4 -> 2 -> None
        Return a pointer to the next node (here: 1)
        """
        if not head:
            return None
        while step > 0 and head:
            prev = head
            head = head.next
            step -= 1
        prev.next = None
        return head

    def getListLength(self, head: ListNode) -> int:
        l = 0
        while head:
            l += 1
            head = head.next
        return l

def print_list(node):
    """
    Print linked list (for debugging purposes)
    """
    seen = set()
    while node:
        if not node in seen:
            seen.add(node)
        else:
            raise Exception
        print(f"{node.val} -> ", end='')
        node = node.next
    print("None")


l = [5, 4, 3, 2, 1, 1]
ll = [ListNode(i) for i in l]
for i in range(len(l) - 1):
    ll[i].next = ll[i + 1]
sol = Solution()
print_list(
    sol.sortList(ll[0])
)