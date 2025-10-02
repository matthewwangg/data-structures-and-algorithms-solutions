class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        std::priority_queue<std::vector<int>> pq;
        std::vector<std::pair<int, int>> neighbors = {std::make_pair(0, 1), std::make_pair(1, 0), std::make_pair(0, -1), std::make_pair(-1, 0)};
        pq.push(std::vector<int>{-grid[0][0], 0, 0});
        int answer = 0;
        while (pq.size() > 0) {
            std::vector<int> current = pq.top();
            pq.pop();

            int water = -current[0];
            int i = current[1];
            int j = current[2];

            answer = std::max(answer, water);
            grid[i][j] = std::numeric_limits<int>::max();

            if (i == grid.size() - 1 && j == grid[0].size() - 1) {
                return answer;
            }

            for (auto [n_i, n_j] : neighbors) {
                if (i + n_i < 0 || j + n_j < 0 || i + n_i >= grid.size() || j + n_j >= grid.size()) {
                    continue;
                }
                pq.push({-grid[i + n_i][j + n_j], i + n_i, j + n_j});
            }
        }

        return 0;
    }
};
