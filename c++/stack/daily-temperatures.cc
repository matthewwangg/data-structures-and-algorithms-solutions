class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::unordered_map<int, int> indexes;

        std::vector<int> stack = {std::numeric_limits<int>::max()};
        std::vector<int> answer;
        for (int i = temperatures.size() - 1; i > -1; --i) {
            while (stack.back() <= temperatures[i]) {
                stack.pop_back();
            }

            int day = stack.back() != std::numeric_limits<int>::max() ? indexes[stack.back()] : i;

            stack.push_back(temperatures[i]);
            indexes[temperatures[i]] = i;

            answer.push_back(day - i);
        }
        std::reverse(answer.begin(), answer.end());
        return answer;
    }
};
