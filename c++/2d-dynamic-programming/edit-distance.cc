class Solution {
public:
    int minDistance(string word1, string word2) {
        std::vector<std::vector<std::optional<int>>> indexes(word1.size(), std::vector<std::optional<int>>(word2.size(), std::nullopt));
        return edit(0, 0, word1, word2, indexes);
    }

private:
    int edit(int i, int j, std::string& word1, std::string& word2, std::vector<std::vector<std::optional<int>>>& indexes) {
        if (i == word1.size() && j == word2.size()) {
            return 0;
        }

        if (i == word1.size() || j == word2.size()) {
            return word1.size() - i + word2.size() - j;
        }

        if (indexes[i][j] != std::nullopt) {
            return indexes[i][j].value();
        }

        if (word1[i] == word2[j]) {
            indexes[i][j] = edit(i + 1, j + 1, word1, word2, indexes);
        } else {
            indexes[i][j] = std::min({edit(i + 1, j, word1, word2, indexes), edit(i + 1, j + 1, word1, word2, indexes), edit(i, j + 1, word1, word2, indexes)}) + 1;
        }

        return indexes[i][j].value();
    }
};
