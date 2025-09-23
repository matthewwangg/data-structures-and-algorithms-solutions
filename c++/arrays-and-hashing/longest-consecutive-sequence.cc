class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> numbers;
        for (int num : nums) {
            numbers.insert(num);
        }

        int answer = 0;
        for (int num : numbers) {
            if (numbers.contains(num - 1)) {
                continue;
            }

            int increment = 0;
            while (numbers.contains(num+increment)) {
                increment++;
            }

            answer = std::max(answer, increment);
        }

        return answer;
    }
};
