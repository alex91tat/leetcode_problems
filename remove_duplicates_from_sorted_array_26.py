# 26. Remove Duplicates from Sorted Array
# Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        j = 1

        for i in range(1, k):
            if nums[i - 1] != nums[i]:
                nums[j] = nums[i]
                j += 1

        return j