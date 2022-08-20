from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max=0
        i=0
        j=len(nums)-1
        while i<=j:
            sum=nums[i]+nums[j]
            if sum>max:
                max=sum
            i+=1
            j-=1
        return max
