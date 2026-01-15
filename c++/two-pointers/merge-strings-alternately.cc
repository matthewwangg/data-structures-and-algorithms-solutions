class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        int i = 0;
        int j = 0;
        std::string merged_string = "";
        bool first = true;

        while (i < m || j < n) {
            if (i == m) {
                merged_string += word2[j];
                j++;
            } else if (j == n) {
                merged_string += word1[i];
                i++;
            } else {
                if (first) {
                    merged_string += word1[i];
                    i++;
                    first = false;
                } else {
                    merged_string += word2[j];
                    j++;
                    first = true;
                }
            }
        }

        return merged_string;
    }
};
