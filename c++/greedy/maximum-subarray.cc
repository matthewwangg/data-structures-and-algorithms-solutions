class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int answer = std::numeric_limits<int>::min();
        int curr = 0;
        for (int num : nums) {
            curr = std::max(num, curr + num);
            answer = std::max(answer, curr);
        }
        return answer;
    }
};
