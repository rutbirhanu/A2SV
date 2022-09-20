class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i=0
        n=[i for i in range(1,n+1)]

        while len(n)>1:
            i=(i+k-1)%len(n)
            n.pop(i)
        return n[0]
