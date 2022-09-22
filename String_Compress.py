from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        count = 0
        alpha = chars[0]

        for i in range(len(chars)):
            if chars[i] == alpha:
                count += 1

            else:
                s += alpha
                if count>1:
                    s += str(count)
                count = 0
                alpha = chars[i]
                count += 1
        s += chars[len(chars) - 1]
        if count > 1:
            s += str(count)
        chars[:] = list(s)
        return len(s)