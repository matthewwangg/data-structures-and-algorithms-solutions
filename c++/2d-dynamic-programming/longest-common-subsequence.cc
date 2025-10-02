class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        std::vector<std::vector<int>> lcs(text1.size(), std::vector<int>(text2.size(), 0));
        bool found = false;
        for (int i = 0; i < text1.size(); ++i) {
            if (text1[i] == text2[0] || found) {
                lcs[i][0] = 1;
                found = true;
            }
        }
        
        found = false;
        for (int j = 0; j < text2.size(); ++j) {
            if (text2[j] == text1[0] || found) {
                lcs[0][j] = 1;
                found = true;
            }
        }

        for (int i = 1; i < text1.size(); ++i) {
            for (int j = 1; j < text2.size(); ++j) {
                if (text1[i] == text2[j]) {
                    lcs[i][j] = lcs[i-1][j-1] + 1;
                } else {
                    lcs[i][j] = std::max(lcs[i-1][j], lcs[i][j-1]);
                }
            }
        }

        return lcs.back().back();
    }
};
