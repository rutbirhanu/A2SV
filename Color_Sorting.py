from typing import List


class Solution:
    def sortColors(self, arr: List[int]) -> None:
        tally=[0]*(max(arr)+1)
        output=[0]*len(arr)
        for i in range(len(arr)):
             tally[arr[i]]+=1

        for i in range(1,len(tally)):
            tally[i]+=tally[i-1]
        for i in range(len(arr)-1,-1,-1):
            val=arr[i]
            tally[val]-=1
            output[tally[val]]=arr[i]
        for i in range(len(arr)):
            arr[i]=output[i]




