struct Solution;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        let mut nums = nums.clone();
        nums.sort();

        for (index, num) in nums.iter().enumerate() {
            if index > 0 && *num == nums[index - 1] {
                continue;
            }
            let mut l = index + 1;
            let mut r = nums.len() - 1;
            
            while l < r {
                let tsum = num + nums[l] + nums[r];
                if tsum > 0 {
                    r -= 1;
                }
                else if tsum < 0 {
                    l += 1;
                } else {
                    res.push(vec![*num , nums[l], nums[r]]);
                    l += 1;
                    while nums[l] == nums[l - 1] && l < r {
                        l += 1;
                    }
                }
                
            }

        }
        return res;
    }
}
