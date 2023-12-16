from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = deque([root])
        while q:
            len_q = len(q)
            prev = None
            for _ in range(len_q):
                cur = q.popleft()
                if cur and cur.left: q.append(cur.left)
                if cur and cur.right: q.append(cur.right)
                if prev: prev.next= cur
                prev = cur
            cur.next = None
        return root
    
    def connect_const_space(self, root: 'Node') -> 'Node':
        node = root
        while node:
            level_ptr = cur = Node(-1)
            while node: # for each node in parent level (until we hit the rightmost node)
                if node.left:
                    cur.next = node.left  # this sets level_ptr to start of level
                    cur = cur.next
                if node.right:
                    cur.next = node.right
                    cur = cur.next
                # all nodes in the parent level had been connected earlier
                node = node.next
            node = level_ptr.next
        return root



root = Node(1)
root.left, root.right = Node(2), Node(3)
root.left.left, root.left.right, root.right.right = Node(4), Node(5), Node(7)
s = Solution()
