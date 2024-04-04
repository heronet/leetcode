class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negs = 0
        for row in grid:
            for i in row:
                if i < 0:
                    negs += 1
        return negs