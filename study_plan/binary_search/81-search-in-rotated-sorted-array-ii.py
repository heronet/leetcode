from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l = l + 1
                r = r - 1
                continue

            # left sorted part
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # right sorted part
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


s = Solution()

print(s.search([2, 5, 6, 0, 0, 1, 2], 0))
