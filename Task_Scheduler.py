from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        count = 0
        list = [counter[i] for i in counter]

        for i, ele in enumerate(list):
            if ele == max(list):
                count += 1
        return max(len(tasks), (max(list) - 1) * (n + 1) + count)
