'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''

def height_(root, h):
    if root.left is None and root.right is None:
        return h
    elif root.left is None and root.right is not None:
        return height_(root.right, h + 1)
    elif root.right is None and root.left is not None:
        return height_(root.left, h + 1)
    else:
        return max(height_(root.left, h + 1), height_(root.right, h + 1))


def height(root):
    return height_(root, 0)