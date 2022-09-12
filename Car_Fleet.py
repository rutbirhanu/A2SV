from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        array=[[i,j] for i,j in zip(position,speed)]
        array.sort(key=lambda x:x[0], reverse=True)

        for i,j in array:
            time=(target-i)/j
            stack.append(time)
            if len(stack)>=2 and stack[-1] <=stack[-2]:
                stack.pop()
        return len(stack)
