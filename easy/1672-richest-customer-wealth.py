from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most = 0
        for m in accounts:
            total = 0
            for n in m:
                total += n
            if total > most:
                most = total
        return most
