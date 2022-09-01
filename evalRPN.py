from typing import List

class Solution:
    def evalRPN(self, token: List[str]) -> int:
        stack = []
        value = ["-", "+", "*", "/"]
        for i in token:
            if i not in value:
                stack.append(int(i))
            if i in value:
                if i == "+":
                    result = stack.pop() + stack.pop()
                elif i == "-":
                    result = stack.pop(-2) - stack.pop(-1)
                elif i == "*":
                    result = stack.pop() * stack.pop()
                elif i == "/":
                    if stack[-1] == 0:
                        return None
                    else:
                        result = stack.pop(-2) / stack.pop(-1)
                stack.append(int(result))
        return stack[0]
