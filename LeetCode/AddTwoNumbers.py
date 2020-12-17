"""
You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number
0 itself.

e.g. `l1 = 2 -> 4 -> 3`, `l2 = 5 -> 6 -> 4` gives `7 -> 0 -> 8`
"""
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        out = []
        prev_carry = 0
        prev_node = None
        while not (curr1 is None and curr2 is None):
            if curr1 is not None and curr2 is not None:
                sum_ = curr1.val + curr2.val + prev_carry

                curr2 = curr2.next
                curr1 = curr1.next
            elif curr1 is None:
                sum_ = curr2.val + prev_carry
                curr2 = curr2.next
            elif curr2 is None:
                sum_ = curr1.val + prev_carry
                curr1 = curr1.next
            carry = sum_ // 10
            digit = sum_ % 10
            node = ListNode(digit)
            out.append(node)
            if prev_node is not None:
                prev_node.next = node

            prev_carry = carry
            prev_node = node

        if prev_carry != 0:
            node = ListNode(prev_carry)
            out.append(node)
            prev_node.next = node
        return out[0]


def _list_nodes_from_list(l) -> List[ListNode]:
    l = list(ListNode(val, None) for val in l)
    for i, node in enumerate(l):
        if i < len(l) - 1:
            node.next = l[i + 1]
    return l


l1 = _list_nodes_from_list([2, 4, 3])
l2 = _list_nodes_from_list([5, 6, 4])
out = Solution().addTwoNumbers(l1[0], l2[0])
