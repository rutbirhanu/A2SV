from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, arr: List[int]) -> List[int]:

        result = []
        arr.sort()
        flag = True
        diction = Counter(arr)
        if len(arr) % 2 != 0:
            return []
        for i in arr:
            if i == 0 and diction[i] >= 2:
                diction[i] -= 2
                result.append(i)
            elif diction[i * 2] > 0 and diction[i] > 0:
                diction[i * 2] -= 1
                diction[i] -= 1
                result.append(i)
            else:
                if diction[i] > 0:
                    flag = False
        return result if flag == True else []


