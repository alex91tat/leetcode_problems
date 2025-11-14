# 169. Majority Element
# Problem link: https://leetcode.com/problems/majority-element/description/
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = -1
        count = 0

        for num in nums:
            if count == 0:
                answer = num

            if num == answer:
                count  += 1
            else:
                count -= 1

        return answer