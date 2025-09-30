class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        std::vector<std::vector<bool>> atlantic(heights.size(), std::vector<bool>(heights[0].size(), false));
        std::vector<std::vector<bool>> pacific(heights.size(), std::vector<bool>(heights[0].size(), false));

        std::vector<std::pair<int, int>> neighbors = {std::make_pair(0, 1), std::make_pair(1, 0), std::make_pair(-1, 0), std::make_pair(0, -1)};

        std::queue<std::pair<int, int>> q;
        for (int i = 0; i < heights.size(); ++i) {
            for (int j = 0; j < heights[0].size(); ++j) {
                if (i == 0 || j == 0) {
                    q.push(std::make_pair(i, j));
                }
            }
        }

        while (q.size() > 0) {
            std::pair<int, int> current = q.front();
            q.pop();

            int i = current.first;
            int j = current.second;

            pacific[i][j] = true;

            for (auto [n_i, n_j] : neighbors) {
                if (i+n_i < 0 || j+n_j < 0 || i+n_i >= heights.size() || j+n_j >= heights[0].size() || pacific[i+n_i][j+n_j] || heights[i+n_i][j+n_j] < heights[i][j]) {
                    continue;
                }
                q.push(std::make_pair(i+n_i, j+n_j));
            }
        }

        for (int i = 0; i < heights.size(); ++i) {
            for (int j = 0; j < heights[0].size(); ++j) {
                if (i == heights.size() - 1 || j == heights[0].size() - 1) {
                    q.push(std::make_pair(i, j));
                }
            }
        }

        while (q.size() > 0) {
            std::pair<int, int> current = q.front();
            q.pop();

            int i = current.first;
            int j = current.second;

            atlantic[i][j] = true;

            for (auto [n_i, n_j] : neighbors) {
                if (i+n_i < 0 || j+n_j < 0 || i+n_i >= heights.size() || j+n_j >= heights[0].size() || atlantic[i+n_i][j+n_j] || heights[i+n_i][j+n_j] < heights[i][j]) {
                    continue;
                }
                q.push(std::make_pair(i+n_i, j+n_j));
            }
        }

        std::vector<std::vector<int>> answer;
        for (int i = 0; i < heights.size(); ++i) {
            for (int j = 0; j < heights[0].size(); ++j) {
                if (pacific[i][j] && atlantic[i][j]) {
                    answer.push_back(std::vector<int>{i, j});
                }
            }
        }

        return answer;
    }
};
