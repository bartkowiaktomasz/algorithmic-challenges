# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # say we're given 2 -> 4 -> 1
        if not head:
            return None
        root = head
        # make a list of 2x size: 2 -> 2' -> 4 -> 4' -> 1 -> 1'
        while head:
            head_cp = Node(head.val)
            next_ = head.next
            head.next = head_cp
            head_cp.next = next_
            head = next_
        head = root
        # Assign random pointers (e.g. if 2.random -> 4 then 2'.random -> 4')
        #  so it's always the node after the random of the original node
        while head:
            head_cp = head.next
            head_cp.random = head.random.next if head.random else None
            next_ = head_cp.next
            head = next_
        head = root
        root_cp = root.next
        head_cp = root_cp
        # Take every other node of the list to build the copy
        while head_cp:
            head_cp.next = head_cp.next.next if head_cp.next else None
            head_cp = head_cp.next
        return root_cp
            
            
            