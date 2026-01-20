class Solution {
public:
    int calPoints(vector<string>& operations) {
        std::vector<int> game_log;
        for (int i = 0; i < operations.size(); ++i) {
            if (operations[i] == "+") {
                int first = game_log[game_log.size() - 1];
                int second = game_log[game_log.size() - 2];
                game_log.push_back(first + second);
            } else if (operations[i] == "D") {
                int first = game_log[game_log.size() - 1];
                game_log.push_back(2 * first);
            } else if (operations[i] == "C") {
                game_log.pop_back();
            } else {
                game_log.push_back(std::stoi(operations[i]));
            }
        }

        return std::accumulate(game_log.begin(), game_log.end(), 0);
    }
};
