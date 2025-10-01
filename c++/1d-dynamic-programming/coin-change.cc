class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        std::vector<int> count(amount + 1, std::numeric_limits<int>::max());
        count[0] = 0;
        for (int coin : coins) {
            for (int i = coin; i < amount + 1; ++i) {
                if (count[i - coin] < std::numeric_limits<int>::max()) {
                    count[i] = std::min(count[i], count[i - coin] + 1);
                }
            }
        }
        
        if (count[amount] == std::numeric_limits<int>::max()) {
            return -1;
        }

        return count[amount];
    }
};
