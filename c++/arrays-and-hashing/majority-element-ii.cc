class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> count;
        std::vector<int> majority_elements;
        int target = int(nums.size() / 3) + 1;

        for (int num : nums) {
            count[num]++;

            if (count[num] == target) {
                majority_elements.push_back(num);
            }
        }

        return majority_elements;
    }
};
