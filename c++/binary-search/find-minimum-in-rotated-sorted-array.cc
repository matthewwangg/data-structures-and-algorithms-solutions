class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        int answer = std::numeric_limits<int>::max();
        while (left <= right) {
            int middle = (left + right) / 2;
            answer = std::min(answer, nums[middle]);

            if (nums[left] <= nums[middle] && nums[right] < nums[left]) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return answer;
    }
};
