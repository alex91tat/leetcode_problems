# 104. Maximum Depth of Binary Tree
# Problem link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

        # Time: O(n)
        # Space: O(h) or O(n) (aprox same thing)