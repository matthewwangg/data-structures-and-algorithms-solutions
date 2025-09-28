class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        std::reverse(word.begin(), word.end());
        std::vector<std::pair<int, int>> options = {std::make_pair(0, 1), std::make_pair(1, 0), std::make_pair(0, -1), std::make_pair(-1, 0)};
        char start = word.back();
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                std::vector<std::vector<int>> visited(board.size(), std::vector<int>(board[0].size(), false));
                if (board[i][j] == start && dfs(i, j, word, board, visited, options)) {
                    return true;
                }
            }
        }
        return false;
    }

private:
    bool dfs(int i, int j, std::string& word, std::vector<std::vector<char>>& board, std::vector<std::vector<int>>& visited, std::vector<std::pair<int, int>>& options) {
        if (word.size() == 0) {
            return true;
        }

        if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size() || visited[i][j] || board[i][j] != word.back()) {
            return false;
        }

        visited[i][j] = true;
        char back = word.back();
        word.pop_back();
        for (auto [n_i, n_j] : options) {
            if (dfs(i+n_i, j+n_j, word, board, visited, options)) {
                return true;
            }
        }
        word.push_back(back);
        visited[i][j] = false;

        return false;
    }
};
