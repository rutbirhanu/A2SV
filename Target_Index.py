from typing import List


class Solution:
    def targetIndices(self, arr: List[int], target: int) -> List[int]:
        arr=sorted(arr)
        result=[]
        for i in range(len(arr)):
            if arr[i]==target:
                result.append(i)
        return result