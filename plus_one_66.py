# 66. Plus One
# Problem link: https://leetcode.com/problems/plus-one/description/
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        for i in range(n, -1, -1):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits

            digits[i] = 0

            if i == 0:
                return [1] + digits