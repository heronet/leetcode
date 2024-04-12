# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    ...

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        x = n
        while l <= r:
            mid = (l + r) // 2
            bad = isBadVersion(mid)

            if bad:
                if mid <= x:
                    x = mid
                r = mid - 1
            else:
                l = mid + 1
        return x