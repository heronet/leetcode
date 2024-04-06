from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # lower bound
        low = 0
        high = len(nums) - 1

        lb = -1

        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                if target == nums[mid]:
                    lb = mid
                high = mid - 1
            else:
                low = mid + 1

        # higher bound
        low = 0
        high = len(nums) - 1
        hb = -1

        while low <= high:
            mid = (low + high) // 2
            if target >= nums[mid]:
                if target == nums[mid]:
                    hb = mid
                low = mid + 1
            else:
                high = mid - 1

        return [lb, hb]


s = Solution()

s.searchRange([5, 7, 7, 8, 8, 10], 8)
