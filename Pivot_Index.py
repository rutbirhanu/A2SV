from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        left_sum = 0
        for i, ele in enumerate(nums):
            right_sum = total - left_sum - ele
            if left_sum == right_sum:
                return i
            left_sum += ele
        return -1

