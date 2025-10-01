class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end());

        int answer = 0;
        int end = std::numeric_limits<int>::min();
        for (std::vector<int> interval : intervals) {
            if (interval[0] < end) {
                answer += 1;
                end = std::min(end, interval[1]);
            } else {
                end = std::max(end, interval[1]);
            }
        }      

        return answer;
    }
};
