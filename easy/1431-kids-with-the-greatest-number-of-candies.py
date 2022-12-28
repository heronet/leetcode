from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        for candy in candies:
            total = candy + extraCandies
            res = True
            for c in candies:
                if c > total:
                    res = False
            arr.append(res)
        return arr
