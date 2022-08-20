from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        current = []
        for i in range(len(l)):
            current = [nums[k] for k in range(l[i], r[i] + 1)]
            current.sort()
            diff = current[1] - current[0]
            check = True
            for i in range(1, len(current)):
                minus = current[i] - current[i - 1]
                if diff != minus:
                    check = False

            if check == True:
                ans.append(True)
            else:
                ans.append(False)
        return ans



