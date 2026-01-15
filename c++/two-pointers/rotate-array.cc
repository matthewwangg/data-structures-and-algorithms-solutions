class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int rotations = k % nums.size();
        std::reverse(nums.begin(), nums.end());

        auto it = nums.begin();
        for (int i = 0; i < rotations; ++i) {
            it++;
        }

        std::reverse(nums.begin(), it);
        std::reverse(it, nums.end());
    }
};
