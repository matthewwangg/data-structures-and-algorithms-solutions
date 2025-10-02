class Solution {
public:
    int numDistinct(string s, string t) {
        std::vector<std::vector<std::optional<int>>> indexes(s.size(), std::vector<std::optional<int>>(t.size(), std::nullopt));
        return construct(0, 0, s, t, indexes);
    }

private:
    int construct(int i, int j, std::string& s, std::string& t, std::vector<std::vector<std::optional<int>>>& indexes) {
        if (j == t.size()) {
            return 1;
        }

        if (i == s.size()) {
            return 0;
        }

        if (indexes[i][j] != std::nullopt) {
            return indexes[i][j].value();
        }

        indexes[i][j] = 0;
        if (s[i] == t[j]) {
            indexes[i][j] = indexes[i][j].value() + construct(i+1, j+1, s, t, indexes);
        }
        indexes[i][j] = indexes[i][j].value() + construct(i+1, j, s, t, indexes);

        return indexes[i][j].value();
    }
};
