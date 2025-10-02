class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        std::vector<std::vector<std::optional<int>>> path(matrix.size(), std::vector<std::optional<int>>(matrix[0].size(), std::nullopt));
        std::vector<std::pair<int, int>> neighbors = {std::make_pair(0, 1), std::make_pair(1, 0), std::make_pair(0, -1), std::make_pair(-1, 0)};

        int answer = 0;
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix[0].size(); ++j) {
                answer = std::max(answer, dfs(i, j, matrix, path, neighbors));
            }
        }
        
        return answer;
    }

private:
    int dfs(int i, int j, std::vector<std::vector<int>>& matrix, std::vector<std::vector<std::optional<int>>>& path, std::vector<std::pair<int, int>>& neighbors) {
        if (path[i][j] != std::nullopt) {
            return path[i][j].value();
        }

        path[i][j] = 1;

        for (auto [n_i, n_j] : neighbors) {
            int new_i = i + n_i;
            int new_j = j + n_j;
            if (new_i < 0 || new_j < 0 || new_i >= matrix.size() || new_j >= matrix[0].size() || matrix[new_i][new_j] <= matrix[i][j]) {
                continue;
            }
            path[i][j] = std::max(path[i][j].value(), dfs(new_i, new_j, matrix, path, neighbors) + 1);
        }

        return path[i][j].value();
    }
};
