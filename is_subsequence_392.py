# 392. Is Subsequence
# Problem link: https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        indx = 0

        for ch in t:
            if ch == s[indx]:
                print(s[indx])
                indx += 1

            if indx == len(s):
                return True

        return False