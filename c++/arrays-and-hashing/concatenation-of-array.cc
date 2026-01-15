class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> answer(2 * n, 0);
        
        for (int i = 0; i < answer.size(); ++i) {
            answer[i] = nums[i % n];
        }

        return answer;
    }
};
