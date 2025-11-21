# 70. Climbing Stairs
# Problem link: https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        prev, cur = 1, 2
        for _ in range(2, n):
            prev, cur = cur, prev + cur

        return cur