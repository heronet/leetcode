class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[len(nums)-1] != nums[len(nums)-2]:
            return nums[len(nums)-1]
        
        l, r = 1, len(nums) - 2

        while l <= r:
            mid = (l + r) // 2
            
            # both left and right elems must be unique if single
            if nums[mid - 1] != nums[mid] and nums[mid + 1] != nums[mid]:
                return nums[mid]
            # starts from odd(0), continues with even, odd pattern
            # if odd
            if mid % 2 != 0:
                # single elem will break the odd even pattern
                if nums[mid] == nums[mid - 1]:
                    # must eliminate left
                    l = mid + 1
                else:
                    # must eliminate right
                    r = mid - 1
            # if even
            else:
                if nums[mid] == nums[mid + 1]:
                    # must eliminate left
                    l = mid + 2
                else:
                    # must eliminate right
                    r = mid - 2
        return -1

s = Solution()

print(s.singleNonDuplicate([1,1,2]))