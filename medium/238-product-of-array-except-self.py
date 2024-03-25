from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        n = 1
        for x in nums:
            n *= x
            pre.append(n)

        post = []
        n = 1
        for x in reversed(nums):
            n *= x
            post.append(n)
        post = post[::-1]
        
        res = []
        for i, n in enumerate(nums):
            res.append((pre[i - 1] if i > 0 else 1) * (post[i + 1] if i < len(post) - 1 else 1))
        
        return res

x = Solution()

x.productExceptSelf([1,2,3,4])