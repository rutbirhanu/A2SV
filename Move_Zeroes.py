from typing import List

def moveZeroes( nums: List[int]):

    j=0
    for i in range(len(nums)):
        if nums[i]:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1



