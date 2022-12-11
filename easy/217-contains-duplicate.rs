struct Solution;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut m_nums = nums.clone();
        m_nums.sort();
        for (i, e) in m_nums.iter().enumerate() {
            if i == m_nums.len() - 1 {
                return false;
            } else if e == &m_nums[i + 1] {
                return true;
            } 
        }
        return false;
    }
}

fn main() {
    let nums = vec![1,2,3,4];
    let res = Solution::contains_duplicate(nums);
    println!("{}", res);
}
