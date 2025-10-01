class Solution {
public:
    int climbStairs(int n) {
        std::vector<int> steps(n, 0);
        steps[0] = 1;
        if (n > 1) {
            steps[1] = 1;
        }
        for (int i = 1; i < n; ++i) {
            steps[i] += steps[i-1];
            if (i > 1) {
                steps[i] += steps[i-2];
            }
        }

        return steps[n-1];
    }
};
