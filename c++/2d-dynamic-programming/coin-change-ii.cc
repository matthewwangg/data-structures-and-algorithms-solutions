class Solution {
public:
    int change(int amount, vector<int>& coins) {
        std::vector<unsigned long long> amounts(amount+1, 0);
        amounts[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i < amount + 1; ++i) {
                amounts[i] += amounts[i - coin];
            }
        }
        return amounts[amount];
    }
};
