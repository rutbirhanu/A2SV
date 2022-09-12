from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        stack=[]
        i=0
        j=len(height)-1

        while i!=j:
            min_val=min(height[i],height[j])
            area=(j-i)*(min_val)
            stack.append(area)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return max(stack)
