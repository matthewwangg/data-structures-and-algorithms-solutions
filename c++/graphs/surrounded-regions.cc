class Solution {
public:
    void solve(vector<vector<char>>& board) {
        std::vector<std::pair<int, int>> neighbors = {std::make_pair(0, 1), std::make_pair(1, 0), std::make_pair(-1, 0), std::make_pair(0, -1)};
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (i == 0 || j == 0 || i == board.size() - 1 || j == board[0].size() - 1) {
                    dfs(i, j, board, neighbors);
                }
            }
        }

        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                if (board[i][j] == '.') {
                    board[i][j] = 'O';
                }
            }
        }
    }

private:
    void dfs(int i, int j, std::vector<std::vector<char>>& board, std::vector<std::pair<int, int>>& neighbors) {
        if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size() || board[i][j] != 'O') {
            return;
        }

        board[i][j] = '.';

        for (auto [n_i, n_j] : neighbors) {
            dfs(i+n_i, j+n_j, board, neighbors);
        }
    }
};
