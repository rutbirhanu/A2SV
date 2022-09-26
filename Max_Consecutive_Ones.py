from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        res = 0

        for i, ele in enumerate(nums):
            k -= (1 - ele)
            if k < 0:
                k += (1 - nums[left])
                left += 1
            res = max(res, i - left + 1)

        return res

