class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s3.size() != s1.size() + s2.size()) {
            return false;
        }
        std::vector<std::vector<std::optional<bool>>> indexes(s1.size(), std::vector<std::optional<bool>>(s2.size(), std::nullopt));
        std::cout << s1.size() << std::endl;
        return interleave(0, 0, s1, s2, s3, indexes);
    }

private:
    bool interleave(int i, int j, std::string& s1, std::string& s2, std::string& s3, std::vector<std::vector<std::optional<bool>>>& indexes) {
        if (i == s1.size() && j == s2.size()) {
            return true;
        }

        if (i == s1.size()) {
            return s2.substr(j, s2.size() - j + 1) == s3.substr(i + j, s3.size() - (i + j) + 1);
        }

        if (j == s2.size()) {
            return s1.substr(i, s1.size() - i + 1) == s3.substr(i + j, s3.size() - (i + j) + 1);
        }

        if (indexes[i][j] != std::nullopt) {
            return indexes[i][j].value();
        }

        indexes[i][j] = false;
        if (i < s1.size() && s3[i+j] == s1[i] && interleave(i+1, j, s1, s2, s3, indexes)) {
            indexes[i][j] = true;
        }

        if (j < s2.size() && s3[i+j] == s2[j] && interleave(i, j+1, s1, s2, s3, indexes)) {
            indexes[i][j] = true;
        }

        return indexes[i][j].value();
    }
};
