class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        l, r = 1, x / 2
        lb = x // 2
        
        while l <= r:
            mid = int((l + r) // 2)
            sq = mid * mid

            if sq == x:
                return mid
            if sq < x:
                lb = mid
                l = mid + 1
            else:
                r = mid - 1
        return lb

s = Solution()
print(s.mySqrt(4))