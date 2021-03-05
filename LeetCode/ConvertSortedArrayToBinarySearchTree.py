from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.sortedArrayToBSTIter(nums)
        
    def sortedArrayToBSTIter(self, nums: List[int]) -> TreeNode:
        """
        Iterative solution
        """
        l, r = 0, len(nums) - 1
        root = TreeNode()
        stack = deque([(root, l, r)])
        while stack:
            node, l, r = stack.pop()
            mid = (l + r) // 2
            node.val = nums[mid]
            if r == l:
                continue
            if r == l + 1:
                node.right = TreeNode(nums[r])
                continue
            if mid > l:
                node.left = TreeNode()
                stack.append((node.left, l, mid - 1))
            if r > mid:
                node.right = TreeNode()
                stack.append((node.right, mid + 1, r))
        return root
        
        
        
    def sortedArrayToBSTRec(self, nums: List[int]) -> TreeNode:
        """
        Recursive solution
        """
        def build(nums: List[int]):
            if not nums:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])    
            else:
                mid = len(nums) // 2
                root = TreeNode(nums[mid])
                root.left = build(nums[:mid])
                root.right = build(nums[mid + 1:])
            return root
        return build(nums)
            
                
nums = [-10, -3, 0, 5, 9]
sol = Solution()
print(
    sol.sortedArrayToBST(nums)
)