class Solution:
    def isValid(self, s: str) -> bool:

        value = {"]": "[", "}": "{", ")": "("}
        stack = []
        for ele in s:
            if ele in value:
                if stack and stack[-1] == value[ele]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        return False if stack else True

