class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());

        std::vector<std::vector<int>> answer;

        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                int left = j + 1;
                int right = nums.size() - 1;

                while (left < right) {
                    long long value = 0LL + nums[i] + nums[j] + nums[left] + nums[right];

                    if (value == target) {
                        answer.push_back(std::vector<int>{nums[i], nums[j], nums[left], nums[right]});
                        left++;
                        right--;
                    } else if (value < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        std::sort(answer.begin(), answer.end());
        answer.erase(std::unique(answer.begin(), answer.end()), answer.end());

        return answer;
    }
};
