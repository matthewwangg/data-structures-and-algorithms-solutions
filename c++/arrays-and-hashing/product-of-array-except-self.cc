class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> prefix = std::vector<int>{1};
        std::vector<int> suffix = std::vector<int>{1};

        int product = 1;
        for (int i = 0; i < nums.size(); ++i) {
            product = product * nums[i];
            prefix.push_back(product);
        }

        product = 1;
        for (int i = nums.size() - 1; i > -1; --i) {
            product = product * nums[i];
            suffix.push_back(product);
        }
        
        prefix.push_back(1);
        suffix.push_back(1);

        std::reverse(suffix.begin(), suffix.end());

        std::vector<int> answer;
        for (int i = 0; i < nums.size(); ++i) {
            answer.push_back(prefix[i] * suffix[i+2]);
        }
        return answer;
    }
};
