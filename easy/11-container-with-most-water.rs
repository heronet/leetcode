struct Solution;
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
       let mut left = 0;
       let mut right = height.len() - 1;
       let mut area = 0;
       while left < right {
            let temp_area: i32 = (right - left) as i32 * std::cmp::min(height[left], height[right]);
            area = std::cmp::max(temp_area, area);
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
       }
       return area;
    }
}
