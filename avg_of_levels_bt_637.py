# 637. Average of Levels in Binary Tree
# Problem link: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        rez = []
        q = deque()
        q.append(root)

        while q:
            avg = 0
            length = len(q)

            for _ in range(length):
                node = q.popleft()
                avg += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            avg /= length
            rez.append(avg)

        return rez