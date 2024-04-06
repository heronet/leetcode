from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negs = 0
        for row in grid:
            low = 0
            high = len(row) - 1

            # by default length of row; useful when no negs
            lower_bound = len(row)

            while low <= high:
                mid = (low + high) // 2
                if row[mid] < 0:
                    lower_bound = mid
                    high = mid - 1
                else:
                    low = mid + 1
            negs += (len(row) - lower_bound)

            return negs


s = Solution()

s.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1],
                 [1, 1, -1, -2], [-1, -1, -2, -3]])
