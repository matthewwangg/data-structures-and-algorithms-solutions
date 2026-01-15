class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> count;
        int majority = nums[0];
        
        for (int num : nums) {
            count[num]++;
            if (count[num] > count[majority]) {
                majority = num;
            }
        }
        
        return majority;
    }
};
