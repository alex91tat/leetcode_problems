# 33. Search in Rotated Sorted Array
# Problem link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        left, right = 0, n

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        min_idx = left

        if min_idx == 0:
            left, right = 0, n
        elif target >= nums[0] and target <= nums[min_idx - 1]:
            left, right = 0, min_idx - 1
        else:
            left, right = min_idx, n

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1