class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        std::unordered_map<int, int> count = {{ 0, 1 }};
        int number = 0;
        int prefix = 0;

        for (int num : nums) {
            prefix += num;
            number += count[prefix - k];
            count[prefix] += 1;
        }

        return number;
    }
};
