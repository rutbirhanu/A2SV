from typing import List

class Solution:
    def numIdenticalPairs(self, arr: List[int]) -> int:
        count=0
        for i in range(len(arr)-1):
            j=i+1
            while j< len(arr):
                if arr[i]==arr[j]:
                    count+=1
                j += 1
        return count