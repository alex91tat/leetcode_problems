# 383. Ransom Note
# Problem link: https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for ch in magazine:
            hash_map[ch] = 1 + hash_map.get(ch, 0)

        for ch in ransomNote:
            if ch not in hash_map or hash_map[ch] <= 0:
                return False

            hash_map[ch] -= 1

        return True