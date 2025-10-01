class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        std::vector<int> lis(nums.size(), 1);
        for (int j = nums.size() - 1; j > -1; --j) {
            for (int i = j + 1; i < nums.size(); ++i) {
                if (nums[j] < nums[i]) {
                    lis[j] = std::max(lis[j], lis[i] + 1);
                }
            }
        }

        int answer = 1;
        for (int result : lis) {
            answer = std::max(answer, result);
        }

        return answer;
    }
};
