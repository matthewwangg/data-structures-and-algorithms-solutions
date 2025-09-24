class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;

        int max_left = height[left];
        int max_right = height[right];

        int water = 0;
        while (left < right) {
            water += std::min(max_left, max_right);
            if (height[left] > height[right]) {
                water -= height[right];
                right -= 1;
                max_right = std::max(max_right, height[right]);
            } else {
                water -= height[left];
                left += 1;
                max_left = std::max(max_left, height[left]);
            }
        }

        return water;
    }
};
