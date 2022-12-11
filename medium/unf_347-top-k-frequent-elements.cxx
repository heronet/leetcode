#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
	public:
		std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
			std::unordered_map<int, size_t> map;
			std::vector<int> topk;
			for(int x: nums)
				++map[x];
			for(auto& pair: map) {
				topk.push_back(pair.)
				--k;
			}
		}
};
