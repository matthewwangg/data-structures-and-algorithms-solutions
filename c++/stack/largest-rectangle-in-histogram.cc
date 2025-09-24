class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int area = 0;
        std::vector<int> stack = {-1};

        for (int i = 0; i < heights.size() + 1; ++i) {
            while (stack.back() > -1 && (i == heights.size() || heights[i] < heights[stack.back()])) {
                int height = heights[stack.back()];
                stack.pop_back();
                int width = i - stack.back() - 1;
                area = std::max(area, height * width);
            }
            stack.push_back(i);
        }

        return area;
    }
};
