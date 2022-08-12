from typing import List

class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort(key=lambda k:k[0])
        result=[arr[0]]
        for start,end in arr[1:]:
            if result[-1][1]>=start:
                result[-1][1]=max(end,result[-1][1])
            else:
                result.append([start,end])
        return result