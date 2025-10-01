class Solution {
public:
    string longestPalindrome(string s) {
        std::string longest_palindrome = "";

        for (int i = 0; i < s.size(); ++i) {
            int size = 0;
            while (i - size >= 0 && i + size < s.size() && s[i - size] == s[i + size]) {
                if (size * 2 + 1 > longest_palindrome.size()) {
                    longest_palindrome = s.substr(i - size, 2 * size + 1);
                }
                size += 1;
            }

            size = 0;
            while (i - size >= 0 && i + size + 1 < s.size() && s[i - size] == s[i + size + 1]) {
                if (size * 2 + 2 > longest_palindrome.size()) {
                    longest_palindrome = s.substr(i - size, 2 * size + 2);
                }
                size += 1;
            }
        }

        return longest_palindrome;
    }
};
