class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        std::vector<std::pair<int, int>> options = {std::make_pair(0, 1), std::make_pair(1, 0), std::make_pair(0, -1), std::make_pair(-1, 0)};
        int answer = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] != '1') {
                    continue;
                }
                answer += 1;
                dfs(i, j, grid, options);
            }
        }
        return answer;
    }

private:
    void dfs(int i, int j, std::vector<std::vector<char>>& grid, std::vector<std::pair<int, int>>& options) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '0';

        for (auto [n_i, n_j] : options) {
            dfs(i+n_i, j+n_j, grid, options);
        }
    }
};
