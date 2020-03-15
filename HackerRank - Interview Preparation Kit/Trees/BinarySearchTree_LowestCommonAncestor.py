'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''


def canReach(root, node):
    # print("Can you reach {} from {}?".format(node, root))
    if root.info == node:
        # print("YES YOU CAN")
        return True
    else:
        # print("left of {} is {} and right is {} ".format(root, root.left, root.right))
        if (root.left is not None and canReach(root.left, node)) or (
                root.right is not None and canReach(root.right, node)):
            # print("You can reach {} from {} !!!".format(root, node))
            return True
        else:
            return False


def canReachBoth(root, v1, v2):
    # print("Checking if you can reach {} and {} from {}".format(v1, v2, root))
    if canReach(root, v1) and canReach(root, v2):
        # print("True")
        return True
    else:
        # print("False")
        return False


def lca_rec(root, v1, v2):
    if root.left is not None and canReachBoth(root.left, v1, v2):
        return lca_rec(root.left, v1, v2)
    elif root.right is not None and canReachBoth(root.right, v1, v2):
        return lca_rec(root.right, v1, v2)
    else:
        return root


def lca(root, v1, v2):
    return lca_rec(root, v1, v2)