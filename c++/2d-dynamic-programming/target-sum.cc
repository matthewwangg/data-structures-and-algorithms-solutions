class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        std::unordered_map<int, std::unordered_map<int, int>> cache;
        return sum(0, target, nums, cache);
    }

private:
    int sum(int i, int target, std::vector<int>& nums, std::unordered_map<int, std::unordered_map<int, int>>& cache) {
        if (i == nums.size() && target == 0) {
            return 1;
        }

        if (i == nums.size()) {
            return 0;
        }

        if (cache.contains(i) && cache[i].contains(target)) {
            return cache[i][target];
        }

        cache[i][target] = sum(i + 1, target - nums[i], nums, cache) + sum(i + 1, target + nums[i], nums, cache);

        return cache[i][target];
    }
};
