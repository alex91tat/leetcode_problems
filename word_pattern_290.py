# 290. Word Pattern
# Problem link: https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w = s.split(" ")
        if len(w) != len(pattern):
            return False

        h1, h2 = {}, {}

        for i in range(len(pattern)):
            if (pattern[i] in h1 and (h1[pattern[i]] != w[i])) or (w[i] in h2 and
            (h2[w[i]] != pattern[i])):
                return False

            h1[pattern[i]] = w[i]
            h2[w[i]] = pattern[i]

        return True

