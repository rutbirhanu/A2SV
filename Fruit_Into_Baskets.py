from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        res=0
        dict={}

        for i,ele in enumerate(fruits):
            dict[ele]=i
            if len(dict)>2:
                min_val=min(dict.values())
                left=min_val+1
                del dict[fruits[min_val]]
            res=max(res,i-left+1)
        return res
