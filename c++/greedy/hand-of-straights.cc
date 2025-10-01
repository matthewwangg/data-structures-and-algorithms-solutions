class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        std::unordered_map<int, int> count;
        for (int card : hand) {
            count[card]++;
        }

        std::sort(hand.begin(), hand.end());
        for (int i = 0; i < hand.size(); ++i) {
            if (count[hand[i]] == 0) {
                continue;
            }
            int update = count[hand[i]];

            for (int j = hand[i]; j < hand[i] + groupSize; ++j) {
                count[j] -= update;
                if (count[j] < 0) {
                    return false;
                }
            }
        }
        return true;
    }
};
