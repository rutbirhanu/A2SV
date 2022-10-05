from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1] * len(nums)
        res=[1]*len(nums)

        for i in range(len(nums)-1):
            ans[i+1]=ans[i]*nums[i]

        for i in range(len(nums)-2,-1,-1):
            res[i]=res[i+1]*nums[i+1]

        for i in range(len(nums)):
            res[i]=res[i]*ans[i]

        return res
