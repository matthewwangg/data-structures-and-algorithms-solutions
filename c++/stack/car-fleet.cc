class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        std::vector<std::pair<int, float>> times;
        for (int i = 0; i < position.size(); ++i) {
            times.push_back(std::make_pair(position[i], static_cast<float>(target - position[i]) / speed[i]));
        }

        std::sort(times.begin(), times.end());
        std::reverse(times.begin(), times.end());

        int answer = 0;
        float time = -1.0;
        
        for (auto [pos, arrival] : times) {
            if (arrival > time) {
                time = arrival;
                answer++;
            }
        }

        return answer;
    }
};
