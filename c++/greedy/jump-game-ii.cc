class Solution {
public:
    int jump(vector<int>& nums) {
        int farthest = 0;
        int next = 0;
        int jumps = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > farthest) {
                farthest = next;
                jumps += 1;
            }
            next = std::max(next, i + nums[i]);
        }
        return jumps;
    }
};
