class Solution {
public:
    int maxProfit(vector<int>& prices) {
        std::unordered_map<int, std::unordered_map<int, int>> cache;
        return stock_decisions(0, -1, prices, cache);
    }

private:
    int stock_decisions(int i, int status, std::vector<int>& prices, std::unordered_map<int, std::unordered_map<int, int>>& cache) {
        if (i == prices.size()) {
            return 0;
        }

        if (cache.contains(i) && cache[i].contains(status)) {
            return cache[i][status];
        }

        if (status == -2) {
            cache[i][status] = stock_decisions(i + 1, -1, prices, cache);
        } else if (status == -1) {
            cache[i][status] = std::max(stock_decisions(i + 1, -1, prices, cache), stock_decisions(i + 1, prices[i], prices, cache));
        } else {
            cache[i][status] = std::max(stock_decisions(i + 1, -2, prices, cache) + (prices[i] - status), stock_decisions(i + 1, status, prices, cache));
        }

        return cache[i][status];
    }
};
