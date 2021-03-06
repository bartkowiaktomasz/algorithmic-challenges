# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')

        def sumNode(node: TreeNode):
            nonlocal max_sum
            if node is None:
                return 0
            left, right = sumNode(node.left), sumNode(node.right)
            node.max_path_sum = max(
                node.val,
                node.val + left,
                node.val + right,
            )
            max_sum = max(
                max_sum,
                node.max_path_sum, 
                node.val + left + right
            )
            return node.max_path_sum

        sumNode(root)
        return max_sum


nums = [TreeNode(i) for i in [-10,9,20,None,None,15,7]]
nums[0].left = nums[1]
nums[0].right = nums[2]
nums[2].left = nums[5]
nums[2].right = nums[6]
sol = Solution()
sol.maxPathSum(nums[0])
