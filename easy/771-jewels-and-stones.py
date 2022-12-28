class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jcount = 0
        for stone in stones:
            if stone in jewels:
                jcount += 1
        return jcount
