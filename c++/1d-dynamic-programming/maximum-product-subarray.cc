class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int answer = std::numeric_limits<int>::min();

        int maximum = 1;
        int minimum = 1;
        for (int num : nums) {
            if (num == 0) {
                maximum = 1;
                minimum = 1;
            } else {
                int old_maximum = maximum;
                maximum = std::max(maximum * num, minimum * num);
                minimum = std::min(minimum * num, old_maximum * num);

                answer = std::max(answer, maximum);
            }
            maximum = std::max(maximum, 1);
            answer = std::max(answer, num);
        }

        return answer;
    }
};
