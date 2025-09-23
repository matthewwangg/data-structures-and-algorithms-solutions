class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::priority_queue<std::tuple<int, int>> pq;
        std::unordered_map<int, int> count;

        for (int num : nums) {
            count[num] += 1;
        }

        for (auto [num, counter] : count) {
            pq.emplace(counter, num);
        }

        std::vector<int> answer;
        for (int i = 0; i < k; ++i) {
            answer.push_back(std::get<1>(pq.top()));
            pq.pop();
        }
        return answer;
    }
};
