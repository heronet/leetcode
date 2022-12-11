from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)
        return list(hashmap.values())


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(["eat","tea","tan"]))
print(Solution().groupAnagrams(["","b",""]))

