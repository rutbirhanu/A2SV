from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = []
        for i, ele in enumerate(citations):
            if ele <= i:
                return i

        return len(citations)
