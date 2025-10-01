class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        std::sort(intervals.begin(), intervals.end());

        std::unordered_map<int, int> indexes;
        for (int i = 0; i < queries.size(); ++i) {
            indexes[i] = queries[i];
        }

        std::sort(queries.begin(), queries.end());
        int index = 0;
        std::priority_queue<std::vector<int>> pq;
        std::unordered_map<int, int> results;
        for (int query : queries) {
            results[query] = -1;
            while (index < intervals.size() && intervals[index][0] <= query) {
                pq.push(std::vector<int>{-(intervals[index][1] - intervals[index][0] + 1), intervals[index][0], intervals[index][1]});
                index++;
            }

            while (pq.size() > 0) {
                std::vector<int> current = pq.top();
                if (current[2] < query) {
                    pq.pop();
                } else {
                    results[query] = -current[0];
                    break;
                }
            }
        }

        std::vector<int> answer;
        for (int i = 0; i < queries.size(); ++i) {
            answer.push_back(results[indexes[i]]);
        }
        
        return answer;
    }
};
