class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        left = 0
        dict = {}

        for i, ele in enumerate(s):
            if ele in dict and dict[ele] >= left:
                left = dict[ele] + 1
            dict[ele] = i
            maxx = max(maxx, i - left + 1)
        return maxx