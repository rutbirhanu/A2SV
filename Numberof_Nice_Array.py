from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        nums = [0 if i % 2 == 0 else 1 for i in nums]
        dict = defaultdict(int)
        dict[0] = 1
        res = 0

        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        for i, ele in enumerate(nums):
            if ele - k in dict:
                res += dict[ele - k]
            dict[ele] += 1

        return res
