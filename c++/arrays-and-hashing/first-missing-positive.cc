class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            while (nums[i] < nums.size() && nums[i] > 0 && nums[i] != nums[nums[i] - 1]) {
                std::swap(nums[nums[i] - 1], nums[i]);
            }
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        
        return nums.size() + 1;
    }
};
