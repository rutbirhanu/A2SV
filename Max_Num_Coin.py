from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        size=len(piles)//3
        piles.sort()
        piles=piles[size:]
        sum=0
        for i in range(0,len(piles),2):
            sum+=piles[i]
        return sum