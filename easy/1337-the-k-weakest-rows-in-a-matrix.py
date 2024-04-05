import collections
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        map = collections.defaultdict(lambda: [])
        for i, row in enumerate(mat):
            count = 0
            for n in row:
                if n == 1: count += 1
            
            map[count].append(i)
    
        res = []
        for i in sorted(map.keys()):
            for n in map[i]:
                res.append(n)
                if len(res) == k:
                    print(res)
                    return res

        return [0]

s = Solution()
# s.kWeakestRows([[1,0],[0,0],[1,0]], 2)
# s.kWeakestRows([[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 3)
s.kWeakestRows([[1,1,0],[1,0,0],[1,0,0],[1,1,1],[1,1,0],[0,0,0]], 4)
# s.kWeakestRows([[0,0], [0,1], [0,0]], 2)