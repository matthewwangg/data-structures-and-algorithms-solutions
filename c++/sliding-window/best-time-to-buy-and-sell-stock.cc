class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min = std::numeric_limits<int>::max();
        int max = std::numeric_limits<int>::min();

        for (int price : prices) {
            max = std::max(max, price - min);
            min = std::min(min, price);
        }

        return std::max(max, 0);
    }
};
