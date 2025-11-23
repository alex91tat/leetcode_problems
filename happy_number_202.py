# 202. Happy Number
# Problem link: https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n) -> int:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit ** 2
                n //= 10

            return sum

        visited = set()

        while n not in visited:
            visited.add(n)

            n = sumOfSquares(n)
            if n == 1:
                return True

        return False