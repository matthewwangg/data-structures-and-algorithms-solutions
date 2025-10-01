class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        std::vector<std::vector<int>> combined_intervals = intervals;        
        std::sort(combined_intervals.begin(), combined_intervals.end());

        std::vector<std::vector<int>> final_intervals = {combined_intervals[0]};
        for (int i = 1; i < combined_intervals.size(); ++i) {
            if (combined_intervals[i][0] <= final_intervals[final_intervals.size() - 1][1]) {
                final_intervals[final_intervals.size() - 1][1] = std::max(final_intervals[final_intervals.size() - 1][1], combined_intervals[i][1]);
            } else {
                final_intervals.push_back(combined_intervals[i]);
            }
        }

        return final_intervals;
    }
};
