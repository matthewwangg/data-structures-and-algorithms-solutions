class Solution {
public:
    int countSubstrings(string s) {
        int palindromes = 0;

        for (int i = 0; i < s.size(); ++i) {
            int size = 0;
            while (i - size >= 0 && i + size < s.size() && s[i - size] == s[i + size]) {
                palindromes += 1;
                size += 1;
            }

            size = 0;
            while (i - size >= 0 && i + size + 1 < s.size() && s[i - size] == s[i + size + 1]) {
                palindromes += 1;
                size += 1;
            }
        }

        return palindromes;
    }
};
