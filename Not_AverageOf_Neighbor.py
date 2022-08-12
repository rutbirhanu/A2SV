from typing import List


class Solution:
    def rearrangeArray(self, arr: List[int]) -> List[int]:
        arr.sort()
        final=[]
        i=0
        j=len(arr)-1
        while len(arr)!=len(final):
            final.append(arr[i])
            i+=1
            if i<=j:
                final.append(arr[j])
                j-=1

        return final