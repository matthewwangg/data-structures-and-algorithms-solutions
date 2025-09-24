class Solution {
public:
    bool isPalindrome(string s) {
        std::string cleaned_s;
        for (int i = 0; i < s.size(); ++i) {
            if (!std::isalnum(s[i])) {
                continue;
            }

            cleaned_s += std::tolower(s[i]);
        }

        std::string reversed_s = cleaned_s;
        std::reverse(reversed_s.begin(), reversed_s.end());

        return cleaned_s == reversed_s;
    }
};
