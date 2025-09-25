class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int fast = 0;
        int slow = 0;
        bool first = true;

        while (first || fast != slow) {
            first = false;
            fast = nums[nums[fast]];
            slow = nums[slow];
        }

        slow = 0;

        while (fast != slow) {
            fast = nums[fast];
            slow = nums[slow];
        }

        return fast;
    }
};
