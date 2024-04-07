from typing import List


class Solution:
    def findPivot(self, nums: List[int]):
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

        return pivot

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        l, r = pivot, len(nums) - 1

        if target > nums[r]:
            l, r = 0, pivot - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:

                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


s = Solution()

s.search([1], 1)
