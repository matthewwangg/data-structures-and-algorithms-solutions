class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        std::unordered_map<int, std::vector<std::vector<int>>> adj;
        for (std::vector<int> flight : flights) {
            adj[flight[0]].push_back({flight[1], flight[2]});
        }

        std::vector<bool> modified(n, false);
        std::vector<std::vector<int>> cost(k + 2, std::vector<int>(n, std::numeric_limits<int>::max()));
        cost[0][src] = 0;
        modified[src] = true;
        for (int i = 1; i < k + 2; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!modified[j] || cost[i-1][j] == std::numeric_limits<int>::max()) {
                    cost[i][j] = std::min(cost[i][j], cost[i-1][j]);
                    continue;
                }

                for (std::vector<int> neighbor : adj[j]) {
                    if (cost[i][neighbor[0]] > cost[i-1][j] + neighbor[1]) {
                        cost[i][neighbor[0]] = cost[i-1][j] + neighbor[1];
                        modified[neighbor[0]] = true;
                    }
                }
                
                if (cost[i][j] < cost[i-1][j]) {
                    modified[j] = true;
                } else {
                    cost[i][j] = cost[i-1][j];
                    modified[j] = false;
                }
            }
        }

        for (int i = 0; i < cost.size(); ++i) {
            for (int j = 0; j < cost[0].size(); ++j) {
                std::cout << cost[i][j] << std::endl;
            }
        }

        if (cost[k+1][dst] == std::numeric_limits<int>::max()) {
            return -1;
        }

        return cost[k+1][dst];
    }
};
