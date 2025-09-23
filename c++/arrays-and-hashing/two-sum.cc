class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> index;

        for (int i = 0; i < nums.size(); ++i) {
            if (index.contains(target - nums[i])) {
                return std::vector<int>{index.at(target - nums[i]), i};
            }
            index[nums[i]] = i;
        }
        return std::vector<int>{};
    }
};
