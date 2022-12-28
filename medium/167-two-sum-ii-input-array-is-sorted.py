from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        diffs = {}
        for index, num in enumerate(numbers):
            diff = target - num
            if num in diffs:
                return [diffs[num], index + 1]
            else:
                diffs[diff] = index + 1
        return []
s = Solution()
ans = s.twoSum([-1,0], -1)
print(ans)

