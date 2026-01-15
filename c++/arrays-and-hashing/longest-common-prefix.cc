class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        std::string shortest = strs[0];

        for (std::string str : strs) {
            if (str.size() < shortest.size()) {
                shortest = str;
            }
        }

        for (int i = 0; i < shortest.size(); ++i) {
            for (std::string str : strs) {
                if (str[i] != shortest[i]) {
                    return shortest.substr(0, i);
                }
            }
        }

        return shortest;
    }
};
