class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int last = nums.size() - 1;
        
        for (int i = 0; i <= last; ++i) {
            while (nums[last] == val && last > i) {
                last--;
            }

            if (nums[i] == val) {
                int temp = nums[i];
                nums[i] = nums[last];
                nums[last] = temp;
                last--;
            }
        }

        return last + 1;
    }
};
