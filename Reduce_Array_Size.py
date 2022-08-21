from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq=Counter(arr)
        sum=count=0
        value_list=[i for i in freq.values()]
        value_list.sort()

        i=len(value_list)-1
        while sum<len(arr)//2:
            sum+=value_list[i]
            i-=1
            count+=1

        return count
