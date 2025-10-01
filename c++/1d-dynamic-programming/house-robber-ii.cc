class Solution {
public:
    int rob(vector<int>& nums) {
        int option_1 = rob_helper(std::vector<int>(nums.begin() + 1, nums.end()));
        int option_2 = rob_helper(std::vector<int>(nums.begin(), nums.end() - 1));
        return std::max({option_1, nums[0], option_2});
    }

private:
    int rob_helper(vector<int> nums) {
        std::vector<int> house(nums.size() + 2, 0);
        for (int i = 2; i < house.size(); ++i) {
            house[i] = std::max(house[i-2] + nums[i-2], house[i-1]);
        }
        return house[house.size() - 1];
    }
};
