# 274. H-Index
# Problem link: https://leetcode.com/problems/h-index/description/
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_count = [0] * (n + 1)

        for citation in citations:
            paper_count[min(n, citation)] += 1

        h = n
        paper = paper_count[n]

        while paper < h:
            h -= 1
            paper += paper_count[h]

        return h