from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, arr: List[int]) -> List[int]:
        final=[]
        for i ,ele in enumerate(arr):
            count = 0
            a=0
            while a<len(arr):
                if ele>arr[a]:
                    count+=1
                a+=1
            final.append(count)

        return final
