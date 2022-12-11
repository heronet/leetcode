struct Solution;
/// <leet>
impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        return s.trim().split_whitespace().last().unwrap().chars().count() as i32;
    }
}
/// </leet>
fn main() {
    let out = Solution::length_of_last_word("Her sdS sDSdSD".to_string());
    println!("{}", out);
}
