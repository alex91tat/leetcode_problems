# 222. Count Complete Tree Nodes
# Problem link: https://leetcode.com/problems/count-complete-tree-nodes/description/
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def heightLeft(root) -> int:
            h = 0
            while root:
                h += 1
                root = root.left

            return h

        def heightRight(root) -> int:
            h = 0
            while root:
                h += 1
                root = root.right

            return h

        if not root: return 0

        left_h = heightLeft(root)
        right_h = heightRight(root)

        if left_h == right_h:
            return 2 ** left_h - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)