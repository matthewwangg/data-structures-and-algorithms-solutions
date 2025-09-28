class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        std::priority_queue<std::pair<int, int>> pq;

        for (int i = 0; i < points.size(); ++i) {
            pq.push(std::make_pair(-(std::pow(points[i][0], 2) + std::pow(points[i][1], 2)), i));
        }

        std::vector<std::vector<int>> answer;
        for (int i = 0; i < k; ++i) {
            answer.push_back(points[pq.top().second]);
            pq.pop();
        }

        return answer;
    }
};
