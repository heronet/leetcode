from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        ans = len(nums)

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans


s = Solution()

s.searchInsert([1, 3, 5, 6], 7)
