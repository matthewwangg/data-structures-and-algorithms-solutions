class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int current = prices[0];

        for (int price : prices) {
            if (price > current) {
                profit += price - current;
                current = price;
            }
            current = std::min(price, current);
        }

        return profit;
    }
};
