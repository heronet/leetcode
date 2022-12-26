#include <string>

class Solution {
public:
    std::string defangIPaddr(std::string address) {
        std::string str;
        for(char ch: address) {
            if(ch != '.')
                str.push_back(ch);
            else {
                str += "[.]";
            }
        }
        return str;
    }
};
