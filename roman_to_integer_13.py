# 13. Roman to Integer
# Problem link: https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        summ, n, i = 0, len(s), 0

        while i < n:
            if i < n - 1 and hash_map[s[i]] < hash_map[s[i + 1]]:
                summ += hash_map[s[i + 1]] - hash_map[s[i]]
                i += 2
            else:
                summ += hash_map[s[i]]
                i += 1

        return summ