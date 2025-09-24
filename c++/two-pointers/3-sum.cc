class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());

        std::vector<std::vector<int>> answer;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    answer.push_back(std::vector<int>{nums[i], nums[left], nums[right]});
                    left += 1;
                    while (nums[left] == nums[left-1] && left < right) {
                        left += 1;
                    }
                } else if (sum < 0) {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }

        return answer;
    }
};
