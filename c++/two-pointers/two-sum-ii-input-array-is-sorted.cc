class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];
            if (sum == target) {
                return std::vector<int>{left+1, right+1};
            } else if (sum > target) {
                right -= 1;
            } else {
                left += 1;
            }
        }

        return std::vector<int>{};
    }
};
