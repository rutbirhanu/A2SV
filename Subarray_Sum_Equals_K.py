from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        freq = {0: 1}

        for i, ele in enumerate(nums):
            sum += ele
            final = sum - k
            if final in freq:
                count += freq[final]
            if sum in freq:
                freq[sum] += 1
            else:
                freq[sum] = 1
        return count

