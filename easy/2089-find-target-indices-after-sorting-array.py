from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        arr = []
        for i, n in enumerate(nums):
            if n == target:
                arr.append(i)
            elif n > target:
                break
        return arr

