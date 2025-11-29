# 151. Reverse Words in a String
# Problem link: https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]

        return ' '.join(reversed_words)