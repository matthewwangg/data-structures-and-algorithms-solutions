class Solution {
public:
    int rob(vector<int>& nums) {
        std::vector<int> house(nums.size() + 2, 0);
        for (int i = 2; i < house.size(); ++i) {
            house[i] = std::max(house[i-2] + nums[i-2], house[i-1]);
        }
        return house[house.size() - 1];
    }
};
