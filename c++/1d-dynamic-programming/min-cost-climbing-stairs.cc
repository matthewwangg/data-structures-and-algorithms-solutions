class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        std::vector<int> min_cost(cost.size() + 1, std::numeric_limits<int>::max());
        min_cost[0] = 0;
        min_cost[1] = 0;
        for (int i = 2; i < min_cost.size(); ++i) {
            min_cost[i] = std::min(min_cost[i], min_cost[i-2] + cost[i-2]);
            min_cost[i] = std::min(min_cost[i], min_cost[i-1] + cost[i-1]);
        }
        return min_cost[cost.size()];
    }
};
