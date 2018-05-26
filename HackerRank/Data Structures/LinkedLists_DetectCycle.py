"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    fast = head
    slow = head

    while(fast):
        slow = slow.next
        if(fast.next):
            fast = fast.next.next
        else:
            return False

        if(slow is fast):
            return True
