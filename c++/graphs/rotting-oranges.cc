class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        std::vector<std::pair<int, int>> neighbors = {std::make_pair(0, 1), std::make_pair(1, 0), std::make_pair(0, -1), std::make_pair(-1, 0)};
        std::queue<std::pair<std::pair<int, int>, int>> q;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 2) {
                    q.push(std::make_pair(std::make_pair(i, j), 0));
                }
            }
        }

        int answer = 0;
        while (q.size() > 0) {
            std::pair<std::pair<int, int>, int> element = q.front();
            q.pop();

            if (element.first.first < 0 || element.first.second < 0 || element.first.first >= grid.size() || element.first.second >= grid[0].size() || grid[element.first.first][element.first.second] == 0) {
                continue;
            }

            grid[element.first.first][element.first.second] = 2;
            answer = std::max(answer, element.second);

            for (auto [n_i, n_j] : neighbors) {
                q.push(std::make_pair(std::make_pair(element.first.first + n_i, element.first.second + n_j), element.second + 1));
            }
            grid[element.first.first][element.first.second] = 0;
        }

        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }
        
        return answer;
    }
};
