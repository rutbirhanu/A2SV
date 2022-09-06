from typing import List


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans=[0]*len(temp)
        mono=[]
        for i,ele in enumerate(temp):
            while mono and ele>temp[mono[-1]]:
                val=mono.pop()
                ans[val]=i-val
            mono.append(i)

        return ans