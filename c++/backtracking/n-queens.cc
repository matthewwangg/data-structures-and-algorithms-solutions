class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        std::vector<std::vector<std::string>> boards;
        std::vector<std::string> board(n, std::string(n, '.'));

        dfs(0, n, board, boards);

        return boards;
    }

private:
    void dfs(int i, int n, std::vector<std::string>& board, std::vector<std::vector<std::string>>& boards) {
        if (i == n) {
            boards.push_back(board);
            return;
        }

        for (int j = 0; j < n; ++j) {
            if (isValid(i, j, n, board)) {
                board[i] = construct(j, n);
                dfs(i+1, n, board, boards);
                board[i] = std::string(n, '.');
            }
        }
    }

    bool isValid(int i, int j, int n, std::vector<std::string>& board) {
        for (int k = 0; k < n; ++k) {
            if (board[i][k] == 'Q') {
                return false;
            }
            if (board[k][j] == 'Q') {
                return false;
            }
            
            std::vector<std::pair<int, int>> neighbors = {std::make_pair(i+k, j+k), std::make_pair(i+k, j-k), std::make_pair(i-k, j-k), std::make_pair(i-k, j+k)};

            for (auto [n_i, n_j] : neighbors) {
                if (n_i < 0 || n_j < 0 || n_i >= board.size() || n_j >= board[0].size()) {
                    continue;
                }

                if (board[n_i][n_j] == 'Q') {
                    return false;
                }
            }
        }
        return true;
    }

    std::string construct(int i, int n) {
        std::string string;
        string.append(i, '.');
        string.append(1, 'Q');
        string.append(n - i - 1, '.');

        return string;
    }
};
