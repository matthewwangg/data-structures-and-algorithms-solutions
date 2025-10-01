class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        std::vector<std::vector<int>> answer;
        int index = 0;
        while (index < intervals.size() && intervals[index][1] < newInterval[0]) {
            answer.push_back(intervals[index]);
            index++;
        }

        std::vector<int> merged = {newInterval[0], newInterval[1]};
        while (index < intervals.size() && intervals[index][0] <= merged[1]) {
            merged[0] = std::min(merged[0], intervals[index][0]);
            merged[1] = std::max(merged[1], intervals[index][1]);
            index++;
        }
        answer.push_back(merged);

        while (index < intervals.size()) {
            answer.push_back(intervals[index]);
            index++;
        }

        return answer;
    }
};
