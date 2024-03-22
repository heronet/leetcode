class Solution {
public:
    int search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        int mid = (start + end) / 2;
        
        while (start <= end) {
            if (nums[mid] > target) {
                end = mid - 1;
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                break;
            }
            mid = (start + end) / 2;
        }
        
        return nums[mid] == target ? mid: -1;
    }
};