#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
	public:
		std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
			std::unordered_map<std::string, std::vector<std::string>> map;
			for(const auto& word: strs) {
				auto key = word;
				std::sort(key.begin(), key.end());
				map[key].push_back(word);
			} 
			std::vector<std::vector<std::string>> vals;
			for(const auto& val: map) {
				vals.push_back(val.second);
			}
			return vals;
		}
};

int main() {
	
}
