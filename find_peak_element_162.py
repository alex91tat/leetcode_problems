# 162. Find Peak Element
# Problem link: https://leetcode.com/problems/find-peak-element/description/
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                r -= 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l += 1
            else:
                return m