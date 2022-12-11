class Solution:
    def isPalindrome(self, s: str) -> bool:
        fresh = ""
        for ch in s:
            if ch.isalnum():
                fresh += ch.lower()
        return fresh == fresh[::-1]
