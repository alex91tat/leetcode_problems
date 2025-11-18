# 80. Remove Duplicates from Sorted Array II
# Problem link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        j = 1
        count = 1

        for i in range(1, k):
            if nums[i - 1] == nums[i]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1

        return j