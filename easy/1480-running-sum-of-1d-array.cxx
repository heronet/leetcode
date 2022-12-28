#include <iostream>
#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> runningSum(std::vector<int>& nums) {
        int total = 0;
        std::vector<int> arr;
        for(int x: nums) {
            total += x;
            arr.push_back(total);
        }
        return arr;
    }
};
