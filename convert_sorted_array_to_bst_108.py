# 108. Convert Sorted Array to Binary Search Tree
# Problem link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divi(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = divi(left, mid - 1)
            root.right = divi(mid + 1, right)

            return root

        return divi(0, len(nums) - 1)