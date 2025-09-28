class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        std::vector<std::vector<int>> permutations;
        construct(permutations, {}, nums);

        return permutations;
    }

private:
    void construct(std::vector<std::vector<int>>& permutations, std::vector<int> permutation, std::vector<int>& nums) {
        if (permutation.size() == nums.size()) {
            permutations.push_back(permutation);
            return;
        }

        for (int num : nums) {
            if (std::find(permutation.begin(), permutation.end(), num) == permutation.end()) {
                permutation.push_back(num);
                construct(permutations, permutation, nums);
                permutation.pop_back();
            }
        }
    }
};
