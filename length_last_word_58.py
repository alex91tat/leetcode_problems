# 58. Length of Last Word
# Problem link: https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strings = s.split()
        if not strings:
            return 0

        return len(strings[-1])
