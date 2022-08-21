from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[[i ,count[i]] for i in count]
        res.sort(key=lambda x:x[1] ,reverse=True)
        ans=[]
        for i in range(k):
            ans.append(res[i][0])
        return ans
