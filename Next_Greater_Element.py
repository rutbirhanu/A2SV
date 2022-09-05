from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        monotonic = [nums2[0]]
        answer = [-1] * len(nums1)

        for i, ele in enumerate(nums2):
            if ele < monotonic[-1]:
                monotonic.append(ele)
            else:
                while monotonic and ele > monotonic[-1]:
                    val = monotonic.pop()
                    if val in nums1:
                        ind = nums1.index(val)
                        answer[ind] = ele
                monotonic.append(ele)

        return answer

