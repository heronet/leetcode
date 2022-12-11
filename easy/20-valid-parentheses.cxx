#include <iostream>
#include <map>
#include <deque>

class Solution {
public:
    bool isValid(std::string s) {
        for (char c : s)
        {
            if (map[c])
            {
                stack.push_back(c);
            }
            else
            {
                char test = stack.empty() ? '#' : *(stack.end() - 1);
                stack.pop_back();
                if(!(c == map[test]))
                {
                    return false;
                }
            }
        }

        return stack.empty();
    }
private:
    std::deque<char> stack;
    std::map<char, char> map{ {'(', ')'}, { '{', '}'}, { '[', ']'} };
};
