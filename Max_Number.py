from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result=Counter(nums)
        count=0
        for ele in nums:
            diff=k-ele

            if diff in result and result[ele]>0 :
                result[ele]-=1

                if result[diff] > 0:
                    result[diff] -= 1
                    count += 1
        return count
