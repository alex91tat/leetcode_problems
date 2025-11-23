# 219. Contains Duplicate II
# Problem link: https://leetcode.com/problems/contains-duplicate-ii/description/
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in hash_map:
                if abs(hash_map[nums[i]] - i) <= k:
                    return True

            hash_map[nums[i]] = i

        return False