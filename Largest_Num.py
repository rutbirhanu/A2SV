from typing import List


class Solution:
    def largestNumber(self, arr: List[int]) -> str:

        arr = [str(arr[i]) for i in range(len(arr))]
        for i in range(len(arr)):
            k = i + 1
            while k < len(arr):
                if arr[i] + arr[k] > arr[k] + arr[i]:
                    k += 1
                else:
                    arr[i], arr[k] = arr[k], arr[i]
                    k += 1
        result = "".join(arr)
        if arr.count("0") == len(arr):
            result = arr[0]

        return result