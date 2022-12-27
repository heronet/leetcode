#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
  public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
      std::unordered_map<int, size_t> count;
      std::vector<std::vector<int>> freq;
      for(int i = 0; i != nums.size() + 1; ++i)
        freq.push_back(std::vector<int>());
      for(int x: nums)
        ++count[x];
      for(const auto& pair: count) {
        freq[pair.second].push_back(pair.first);
      }
      std::reverse(freq.begin(), freq.end());
      std::vector<int> result;
      for(const auto&vec: freq) {
        for(int x: vec) {
          if (result.size() == k)
            return result;
          result.push_back(x);
        }
      }
      return result;
    }
};

    int main() {
      Solution s;
      std::vector<int> vec{1,1,1,2,2,3};
      s.topKFrequent(vec, 2);
    }
