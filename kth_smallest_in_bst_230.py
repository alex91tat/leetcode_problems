# 230. Kth Smallest Element in a BST
# Problem link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        rez = root.val

        def dfs(node):
            nonlocal count, rez
            if not node:
                return

            dfs(node.left)
            count -= 1

            if count == 0:
                rez = node.val
                return

            dfs(node.right)

        dfs(root)
        return rez