class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int left = 0;
        int right = n - 1;
        for (int i = 0; i <= right; ++i) {
            while (nums[i] == 2) {
                nums[i] = nums[right];
                nums[right] = 2;
                right--;

                if (i > right) {
                    return;
                } 
            }
            
            while (nums[i] == 0) {
                nums[i] = nums[left];
                nums[left] = 0;
                left++;

                if (left > i) {
                    break;
                }
            }
        }
    }
};
