# 189. Rotate Array
# Problem link: https://leetcode.com/problems/rotate-array/description/
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        l, r= 0 , n - 1

        def switch(nums: List[int], l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        switch(nums, l, r)
        switch(nums, 0, k - 1)
        switch(nums, k, n - 1)