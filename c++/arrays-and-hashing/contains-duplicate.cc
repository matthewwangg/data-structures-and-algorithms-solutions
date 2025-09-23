class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_map<int, bool> exists;
        for (int i = 0; i < nums.size(); ++i) {
            if (exists.contains(nums[i]) && exists.at(nums[i])) {
                return true;
            }
            exists[nums[i]] = true;
        }
        return false;
    }
};
