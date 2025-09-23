class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_set<char> characters;

        std::vector<std::tuple<int, int>> centers = {std::make_tuple(1, 1), std::make_tuple(1, 4), std::make_tuple(1, 7), std::make_tuple(4, 1), std::make_tuple(4, 4), std::make_tuple(4, 7), std::make_tuple(7, 1), std::make_tuple(7, 4), std::make_tuple(7, 7)};
        std::vector<std::tuple<int, int>> boxes = {std::make_tuple(0, 1), std::make_tuple(0, 0), std::make_tuple(0, -1), std::make_tuple(1, 1), std::make_tuple(1, -1), std::make_tuple(1, 0), std::make_tuple(-1, 1), std::make_tuple(-1, 0), std::make_tuple(-1, -1)};

        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[0].size(); ++j) {
                if (board[i][j] != '.' && characters.contains(board[i][j])) {
                    return false;
                }
                characters.insert(board[i][j]);
            }
            characters.clear();
        }

        for (int i = 0; i < board[0].size(); ++i) {
            for (int j = 0; j < board.size(); ++j) {
                if (board[j][i] != '.' && characters.contains(board[j][i])) {
                    return false;
                }
                characters.insert(board[j][i]);
            }
            characters.clear();
        }

        for (auto [i, j] : centers) {
            for (auto [n_i, n_j] : boxes) {
                if (board[i+n_i][j+n_j] != '.' && characters.contains(board[i+n_i][j+n_j])) {
                    return false;
                }
                characters.insert(board[i+n_i][j+n_j]);
            }
            characters.clear();
        }

        return true;
    }
};
