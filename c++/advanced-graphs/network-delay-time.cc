class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        std::unordered_map<int, std::vector<std::pair<int, int>>> adj;
        for (std::vector<int> time : times) {
            adj[time[0]].push_back(std::make_pair(-time[2], time[1]));
        }

        std::priority_queue<std::pair<int, int>> pq;
        pq.push(std::make_pair(0, k));
        std::unordered_set<int> visited;
        int delay = 0;
        while (pq.size() > 0) {
            std::pair<int, int> current = pq.top();
            pq.pop();

            if (visited.contains(current.second)) {
                continue;
            }

            visited.insert(current.second);
            delay = std::max(delay, -current.first);

            if (visited.size() == n) {
                return delay;
            }

            for (auto [delay, destination] : adj[current.second]) {
                pq.push(std::make_pair(current.first + delay, destination));
            }
        }

        return -1;
    }
};
