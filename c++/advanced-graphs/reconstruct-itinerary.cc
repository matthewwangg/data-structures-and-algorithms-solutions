class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        std::unordered_map<std::string, std::vector<std::string>> adj;
        for (std::vector<std::string> ticket : tickets) {
            adj[ticket[0]].push_back(ticket[1]);
        }

        for (auto [from, to] : adj) {
            std::sort(adj[from].begin(), adj[from].end());
            std::reverse(adj[from].begin(), adj[from].end());
        }

        std::vector<std::string> answer;
        dfs("JFK", answer, adj);
        std::reverse(answer.begin(), answer.end());

        return answer;
    }

private:
    void dfs (std::string location, std::vector<std::string>& answer, std::unordered_map<std::string, std::vector<std::string>>& adj) {
        while (adj[location].size() > 0) {
            std::string next = adj[location].back();
            adj[location].pop_back();
            dfs(next, answer, adj);
        }
        answer.push_back(location);
    }
};
