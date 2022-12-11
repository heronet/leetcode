from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = int(0)
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

print(Solution().search([-1,0,3,5,9,12], 9))
