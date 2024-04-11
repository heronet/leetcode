class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        pivot = -1

        while l <= r:
            mid = (l + r) // 2
            
            # non sorted part; pivot must be here
            if nums[0] >= nums[mid]:
                
                r = mid - 1
            else:
                l = mid + 1
            
            pivot = l
        print(pivot)

        if target <= nums[len(nums) - 1]:
            l, r = pivot, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        else:
            l, r = 0, pivot - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        return False
    
s = Solution()
print(s.search([1,0,1,1,1], 0))