class Solution:
    def calculate(self, s: str) -> int:
        operation_stack=["+","-","*","/"]
        curr=0
        ans=[]
        operator="+"

        for i in range(len(s)):
            ele=s[i]
            if ele.isdigit():
                curr=curr*10+int(ele)
            if ele in operation_stack or i==len(s)-1:
                if operator=="+":
                    ans.append(curr)
                elif operator=="-":
                    ans.append(-curr)
                elif operator=="*":
                    ans[-1]*=curr
                elif operator=="/":
                    ans[-1]=int(ans[-1]/curr)
                curr=0
                operator=ele
        return sum(ans)
