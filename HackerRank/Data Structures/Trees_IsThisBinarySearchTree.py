""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return checkBSTRecursive(root)

def checkBSTRecursive(root, min=None, max=None):
    if not root:
        return True
    if min is not None and root.data <= min:
        return False
    if max is not None and root.data >= max:
        return False
    return checkBSTRecursive(root.right, root.data, max) and checkBSTRecursive(root.left, min, root.data)
