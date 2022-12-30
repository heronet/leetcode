#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> diffs;
        for(int i = 0; i != nums.size(); ++i) {
            int diff = target - nums[i];
            if(diffs.find(diff) != diffs.end()) {
                return std::vector<int> {diffs[diff], i};
            }
            diffs[nums[i]] = i;
        }
        return std::vector<int>();
    }
};
