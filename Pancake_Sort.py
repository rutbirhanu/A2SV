from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        if sorted(arr)==arr:
            return []
        else:
            for i in range(len(arr)):
                curr_max = max(arr)
                ind = arr.index(curr_max)
                ans.append(ind+1)
                arr=arr[ind::-1]+arr[ind+1:]
                arr=arr[::-1]
                ans.append(len(arr))
                arr.remove(curr_max)
            return ans
