class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        res=""
        for i in range(len(s)) :
            if s[i] =="(":
                stack.append(i)
            elif s[i]==")":
                temp=s[stack[-1]:i+1]
                s=s[:stack[-1]]+temp[::-1]+s[i+1:]

                stack.pop()

        for i in s:
            if i !="(" and i!=")":
                res+=i

        return res
