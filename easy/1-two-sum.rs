use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut diffs: HashMap<i32, i32>= HashMap::new();
        for (i, n) in nums.iter().enumerate() {
            let diff = target - n;
            if diffs.contains_key(&diff) {
                return vec![i as i32, diffs[&diff]];
            }
            diffs.insert(*n, i as i32);
        }
        return vec![];
    }
}

fn main() {

}
