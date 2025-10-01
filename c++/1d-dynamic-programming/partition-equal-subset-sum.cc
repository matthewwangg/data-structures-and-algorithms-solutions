class Solution {
public:
    bool canPartition(vector<int>& nums) {
        float target = 0.0f;
        for (int num : nums) {
            target += static_cast<float>(num);
        }
        target = target / 2.0f;

        if (target != static_cast<int>(target)) {
            return false;
        }
        std::vector<std::vector<std::optional<bool>>> cache(nums.size(), std::vector<std::optional<bool>>(static_cast<int>(target+1), std::nullopt));

        return partition(0, target, nums, cache);
    }

private:
    bool partition(int i, int target, std::vector<int>& nums, std::vector<std::vector<std::optional<bool>>>& cache) {
        if (target == 0) {
            return true;
        }

        if (i == nums.size() || target < 0) {
            return false;
        }

        if (cache[i][target] != std::nullopt) {
            return cache[i][target].value();
        }

        cache[i][target] = partition(i+1, target - nums[i], nums, cache) || partition(i+1, target, nums, cache);

        return cache[i][target].value();
    }
};
