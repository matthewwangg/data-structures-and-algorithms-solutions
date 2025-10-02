class Solution {
public:
    int maxCoins(vector<int>& nums) {
        std::unordered_map<int, std::unordered_map<int, int>> cache;
        std::vector<int> balloons = {1};
        for (int num : nums) {
            balloons.push_back(num);
        }
        balloons.push_back(1);
        return burst_balloons(0, balloons.size() - 1, balloons, cache);
    }

private:
    int burst_balloons(int left, int right, std::vector<int>& nums, std::unordered_map<int, std::unordered_map<int, int>>& cache) {
        if (left == right) {
            return 0;
        }

        if (cache.contains(left) && cache[left].contains(right)) {
            return cache[left][right];
        }   

        cache[left][right] = 0;
        for (int i = left + 1; i < right; ++i) {
            cache[left][right] = std::max(cache[left][right], nums[left] * nums[right] * nums[i] + burst_balloons(left, i, nums, cache) + burst_balloons(i, right, nums, cache));
        }

        return cache[left][right];
    }
};
