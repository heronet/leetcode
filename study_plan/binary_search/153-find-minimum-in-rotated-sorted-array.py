from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        pivot = 0

        while l <= r:
            mid = (l + r) // 2

            # before pivot
            if nums[0] <= nums[mid]:
                l = mid + 1
            else:
                pivot = mid
                r = mid - 1

        return nums[pivot]


s = Solution()

s.findMin([11, 13, 15, 17])
