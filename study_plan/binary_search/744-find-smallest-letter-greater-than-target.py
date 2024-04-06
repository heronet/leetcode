from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1

        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if ord(letters[mid]) > ord(target):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return letters[ans]


s = Solution()

s.nextGreatestLetter(["c", "f", "j"], 'k')
