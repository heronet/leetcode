import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        res = end

        while start <= end:
            k = (start + end) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                end = k - 1
            else:
                start = k + 1

        return res


s = Solution()

print(s.minEatingSpeed([3, 6, 7, 11], 8))
