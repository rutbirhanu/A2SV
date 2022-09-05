class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        mono=[]
        for i ,ele in enumerate(num):
            while mono and ele < mono[-1] and k > 0:
                mono.pop()
                k -= 1
            mono.append(ele)
        if k>0:
            mono=mono[:len(mono)-k]
        res="".join(mono)
        return str(int(res)) if res else "0"
