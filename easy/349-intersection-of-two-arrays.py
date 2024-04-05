from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        
        set1 = list(set(sorted(nums1)))
        set2 = list(set(sorted(nums2)))

        if len(set1) >= len(set2):
            for n in set2:
                if n in set1:
                    nums.append(n)
        else:
            for n in set1:
                if n in set2:
                    nums.append(n)
        return nums
