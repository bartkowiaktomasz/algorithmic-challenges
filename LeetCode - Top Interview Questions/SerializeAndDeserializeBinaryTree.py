# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"{self.val}"

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        Args:
            root (TreeNode): Tree root node

        Returns:
            str: Serialized string representation
        """
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is not None:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "|".join(res)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        Args:
            data (str): Serialized tree

        Returns:
            TreeNode: Deserialized tree node
        """
        vals = data.split("|")
        root_val = vals.pop(0)
        queue = [None if root_val == "null" else TreeNode(int(root_val))]
        root = queue[0]
        while vals:
            node = queue.pop(0)
            if node is not None:
                left_val = vals.pop(0)
                right_val = vals.pop(0)
                node.left = None if left_val == "null" else TreeNode(int(left_val))
                node.right = None if right_val == "null" else TreeNode(int(right_val))
                queue.append(node.left)
                queue.append(node.right)
        return root

        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
# Your Codec object will be instantiated and called as such:
codec = Codec()
data = codec.serialize(root)
print(data)
print(codec.deserialize(data))