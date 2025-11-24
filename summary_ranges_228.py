# 228. Summary Ranges
# Problem link: https://leetcode.com/problems/summary-ranges/description/
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rez = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                i += 1

            if start != nums[i]:
                rez.append(str(start) + '->'+ str(nums[i]))
            else:
                rez.append(str(start))

            i += 1

        return rez
