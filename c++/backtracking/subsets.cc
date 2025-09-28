class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        std::vector<std::vector<int>> answer;
        construct(0, nums, answer, {});
        return answer;
    }

private:
    void construct(int i, std::vector<int>& nums, std::vector<std::vector<int>>& answer, std::vector<int> current) {
        answer.push_back(current);

        for (int index = i; index < nums.size(); ++index) {
            current.push_back(nums[index]);
            construct(index + 1, nums, answer, current);
            current.pop_back();
        }
    }
};
