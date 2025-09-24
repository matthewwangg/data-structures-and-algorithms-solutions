class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_water = 0;
        int left = 0;
        int right = height.size() - 1;

        while (left < right) {
            max_water = std::max(max_water, std::min(height[left], height[right]) * (right - left));

            if (height[left] < height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return max_water;
    }
};
