from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        j=0
        for i ,ele in enumerate(pushed):
            while stack and stack[-1]==popped[j]:
                j += 1
                stack.pop()
            stack.append(ele)

        while stack :
            if stack[-1]==popped[j]:
                stack.pop()
                j+=1
            else:
                break
        return False if stack else True

